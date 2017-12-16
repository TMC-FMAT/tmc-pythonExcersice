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


@points('23')
class MainTest(unittest.TestCase):
    __qualname__ = 'MainTest'

    def test_01(self):
        logic_works(self, 1, 2, 3)
        logic_works(self, -1, 2, 3)
        logic_works(self, 1, 2, -4)
        logic_works(self, 111, 12, 114)


def logic_works(test, a, b, c):
    with mock.patch('__builtin__.raw_input', side_effect=[a, b, c]):
        captured_output = StringIO.StringIO()
        sys.stdout = captured_output

        main()
        sys.stdout = sys.__stdout__

        test.assertTrue((len(captured_output.getvalue()) > 0), msg="You did not ask anything!")

        test.assertTrue(("um:" in captured_output.getvalue()),
                        msg="You should output \"Sum: RESULT\" to print the result. You printed: "
                            + captured_output.getvalue())

        test_sum = captured_output.getvalue()[captured_output.getvalue().index('um:') + len('um: '):]
        correct_sum = a + b + c
        test.assertTrue(str(correct_sum) in captured_output.getvalue(), msg=str(a) + " + " + str(b) + " + " + str(c) +
                                                " should be: " + str(correct_sum) + " you proposed: " + test_sum)


if __name__ == '__main__':
    unittest.main()
