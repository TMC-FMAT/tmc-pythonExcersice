#!/usr/bin/env python2
import unittest
import io
import sys
import mock
import StringIO
from tmc import points
from tmc.utils import load, get_stdout
sys.path.append('../')
main = load('src.main', 'main')


@points('30')
class MainTest(unittest.TestCase):
    __qualname__ = 'MainTest'

    def test_01(self):
        logic_works(self, 2)
        logic_works(self, 5)
        logic_works(self, 25)


def logic_works(test, a):
    with mock.patch('__builtin__.raw_input', side_effect=[a]):
        captured_output = StringIO.StringIO()
        sys.stdout = captured_output

        main()
        sys.stdout = sys.__stdout__

        test.assertTrue((len(captured_output.getvalue()) > 0), msg="You did not ask anything!")

        test.assertTrue(("rial: " in captured_output.getvalue()),
                        msg="You should output \"Factorial: RESULT\" to print the result. You printed: "
                            + captured_output.getvalue())

        count = 1
        factorial = 1
        while count <= int(a):
            factorial = factorial * count
            count = count + 1

        test_result = captured_output.getvalue()[captured_output.getvalue().index('rial: ') + len('rial: '):]
        correct_answer = factorial
        test.assertTrue(str(correct_answer) in captured_output.getvalue(),
                        msg="The factorial of " + str(a) + " is: " + str(
                            correct_answer) + " you proposed: " + test_result)


if __name__ == '__main__':
    unittest.main()
