#!/usr/bin/env python2
import unittest
import io
import sys
import mock

sys.path.append('../')
import StringIO
from tmc import points
import math
from src.Circumference import circumference


@points('10')
class CircumferenceTestCase(unittest.TestCase):
    __qualname__ = "CircumferenceTest"

    def test_circumference(self):
        circumference_works(self, 3)


def circumference_works(test, a):
    with mock.patch('__builtin__.raw_input', side_effect=[a]):
        captured_output = StringIO.StringIO()
        sys.stdout = captured_output

        circumference()
        sys.stdout = sys.__stdout__

        test.assertTrue((len(captured_output.getvalue()) > 0), msg="You did not ask anything!")

        test.assertTrue(("ference:" in captured_output.getvalue()),
                        msg="You should output \"Circumference: RESULT\" to print the result. You printed: "
                            + captured_output.getvalue())

        test_result = captured_output.getvalue()[captured_output.getvalue().index('rence: ') + len('rence: '):]
        correct_answer = float(a) * math.pi * 2
        test.assertTrue(str(correct_answer) in captured_output.getvalue(),
                        msg="Circumference with " + str(a) + " radio should be: " + str(
                            correct_answer) + " you proposed: " + test_result)


if __name__ == '__main__':
    unittest.main()
