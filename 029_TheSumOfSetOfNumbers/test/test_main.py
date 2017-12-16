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


@points('29')
class MainTest(unittest.TestCase):
    __qualname__ = 'MainTest'

    def test_01(self):
        logic_works(self, 10)
        logic_works(self, 3)
        logic_works(self, 0)


def logic_works(test, a):
    with mock.patch('__builtin__.raw_input', side_effect=[a]):
        captured_output = StringIO.StringIO()
        sys.stdout = captured_output

        main()
        sys.stdout = sys.__stdout__

        test.assertTrue((len(captured_output.getvalue()) > 0), msg="You did not ask anything!")

        test.assertTrue(("um: " in captured_output.getvalue()),
                        msg="You should output \"Sum: RESULT\" to print the result. You printed: "
                            + captured_output.getvalue())

        cont = 1
        total = 0
        while cont <= int(a):
            total = total + cont
            cont = cont + 1

        test_result = captured_output.getvalue()[captured_output.getvalue().index('um: ') + len('um: '):]
        correct_answer = total
        test.assertTrue(str(correct_answer) in captured_output.getvalue(),
                        msg="The sum of all the numbers is: " + str(
                            correct_answer) + " you proposed: " + test_result)


if __name__ == '__main__':
    unittest.main()
