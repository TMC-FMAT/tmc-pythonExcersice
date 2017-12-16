#!/usr/bin/env python2
import unittest
import io
import sys
import mock

sys.path.append('../')
import StringIO
from tmc import points
from src.BiggerNumber import bigger_number


@points('9.0')
class BiggerNumberTestCase(unittest.TestCase):
    __qualname__ = "BiggerNumberTest"

    def test_bigger_number(self):
        bigger_number_works(self, 6, 2)
        bigger_number_works(self, -6, -2)
        bigger_number_works(self, 6, -2)
        bigger_number_works(self, 6, 6)


def bigger_number_works(test, a, b):
    with mock.patch('__builtin__.raw_input', side_effect=[a, b]):
        captured_output = StringIO.StringIO()
        sys.stdout = captured_output

        bigger_number()
        sys.stdout = sys.__stdout__

        test.assertTrue((len(captured_output.getvalue()) > 0), msg="You did not ask anything!")

        test.assertTrue(("mber: " in captured_output.getvalue()),
                        msg="You should output \"Bigger number: RESULT\" to print the result. You printed: "
                            + captured_output.getvalue())

        test_result = captured_output.getvalue()[captured_output.getvalue().index('mber: ') + len('mber: '):]
        correct_answer = max(a, b)
        test.assertTrue(str(correct_answer) in captured_output.getvalue(),
                        msg=str(a) + ", " + str(b) + " bigger number should be: " + str(
                            correct_answer) + " you proposed: " + test_result)


if __name__ == '__main__':
    unittest.main()
