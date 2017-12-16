#!/usr/bin/env python2
import unittest
import io
import sys
import mock

sys.path.append('../')
import StringIO
from tmc import points
from src.GreaterNumber import greater_number


@points('10')
class GreaterNumber(unittest.TestCase):
    __qualname__ = "GreaterNumberTest"

    def test_greater_number(self):
        solution_works(self, 3, 5)
        solution_works(self, 3, 3)
        solution_works(self, 5, 3)


def solution_works(test, a, b):
    with mock.patch('__builtin__.raw_input', side_effect=[a, b]):
        captured_output = StringIO.StringIO()
        sys.stdout = captured_output

        greater_number()
        sys.stdout = sys.__stdout__

        test.assertTrue((len(captured_output.getvalue()) > 0), msg="You did not print anything!")

        if a == b:
            test.assertTrue(("equal" in captured_output.getvalue()),
                            msg="You should output  \"The numbers are equal\" when the numbers are equal, you printed: "
                                + captured_output.getvalue())

        else:
            test.assertTrue(("number: " in captured_output.getvalue()),
                            msg="You should output \"Greater number: RESULT\" to print the result. You printed: "
                                + captured_output.getvalue())
            test_result = captured_output.getvalue()[captured_output.getvalue().index('ber: ') + len('ber: '):]

            if a > b:
                correct_answer = a

            else:
                correct_answer = b

            test.assertTrue(str(correct_answer) in captured_output.getvalue(),
                        msg='The bigger of the numbers ' + str(a) + ' and ' + str(b) + " is " + str(correct_answer) +
                            " you proposed: " + test_result)


if __name__ == '__main__':
    unittest.main()
