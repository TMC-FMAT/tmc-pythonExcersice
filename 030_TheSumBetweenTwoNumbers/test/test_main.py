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
        logic_works(self, 2, 5)


def logic_works(test, a, b):
    with mock.patch('__builtin__.raw_input', side_effect=[a, b]):
        captured_output = StringIO.StringIO()
        sys.stdout = captured_output

        main()
        sys.stdout = sys.__stdout__

        test.assertTrue((len(captured_output.getvalue()) > 0), msg="You did not ask anything!")

        test.assertTrue(("um: " in captured_output.getvalue()),
                        msg="You should output \"Sum: RESULT\" to print the result. You printed: "
                            + captured_output.getvalue())

        total = 0
        while a <= b:
            total = total + a
            a = a + 1

        test_result = captured_output.getvalue()[captured_output.getvalue().index('um: ') + len('um: '):]
        correct_answer = total
        test.assertTrue(str(correct_answer) in captured_output.getvalue(),
                        msg="The sum form " + str(a) + " to " + str(b) + " is: " + str(
                            correct_answer) + " you proposed: " + test_result)


if __name__ == '__main__':
    unittest.main()
