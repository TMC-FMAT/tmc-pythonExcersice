#!/usr/bin/env python2
import unittest
import io
import sys
import mock

sys.path.append('../')
import StringIO
from tmc import points
import math
from src.GradesAndPoints import grades_and_points


@points('18')
class GradesAndPointsTestCase(unittest.TestCase):
    __qualname__ = "GradesAndPointsTest"

    def test_circumference(self):
        grades_and_points_works(self, 0)
        grades_and_points_works(self, 59)
        grades_and_points_works(self, 60)
        grades_and_points_works(self, 90)


def grades_and_points_works(test, a):
    with mock.patch('__builtin__.raw_input', side_effect=[a]):
        captured_output = StringIO.StringIO()
        sys.stdout = captured_output

        grades_and_points()
        sys.stdout = sys.__stdout__

        test.assertTrue((len(captured_output.getvalue()) > 0), msg="You did not ask anything!")

        test.assertTrue(("atus:" in captured_output.getvalue()),
                        msg="You should output \"Status: approved/failed\" to print the result. You printed: "
                            + captured_output.getvalue())

        test_result = captured_output.getvalue()[captured_output.getvalue().index('tus: ') + len('tus: '):]

        if int(a) > 59:
            correct_answer = 'approved'

        else:
            correct_answer = 'failed'

        test.assertTrue(correct_answer in captured_output.getvalue(),
                        msg="A note with " + str(a) + " points should be: " + str(
                            correct_answer) + " you proposed: " + test_result)


if __name__ == '__main__':
    unittest.main()
