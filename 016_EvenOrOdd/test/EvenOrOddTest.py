#!/usr/bin/env python2
import unittest
import io
import sys
import mock

sys.path.append('../')
import StringIO
from tmc import points
from src.EvenOrOdd import even_or_odd


@points('10')
class EvenOrOdd(unittest.TestCase):
    __qualname__ = "EvenOrOddTest"

    def test_even_or_odd(self):
        solution_works(self, 3)


def solution_works(test, a):
    with mock.patch('__builtin__.raw_input', side_effect=[a]):
        captured_output = StringIO.StringIO()
        sys.stdout = captured_output

        even_or_odd()
        sys.stdout = sys.__stdout__

        test.assertTrue((len(captured_output.getvalue()) > 0), msg="You did not print anything!")

        test.assertTrue(("is " in captured_output.getvalue()),
                        msg="You should output \"Number INPUT is odd/even\" to print the result. You printed: "
                            + captured_output.getvalue())

        test_result = captured_output.getvalue()[captured_output.getvalue().index('is ') + len('is '):]

        if a % 2 == 0:
            correct_answer = 'even'

        else:
            correct_answer = 'odd'

        test.assertTrue(correct_answer in captured_output.getvalue(),
                        msg="Number " + str(a) + " is " + str(
                            correct_answer) + " you proposed: " + test_result)


if __name__ == '__main__':
    unittest.main()
