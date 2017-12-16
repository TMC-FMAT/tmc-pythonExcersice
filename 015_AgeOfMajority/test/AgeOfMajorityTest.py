#!/usr/bin/env python2
import unittest
import io
import sys
import mock

sys.path.append('../')
import StringIO
from tmc import points
import math
from src.AgeOfMajority import age_of_majority


@points('10')
class AgeOfMajorityTestCase(unittest.TestCase):
    __qualname__ = "AgeOfMajorityTest"

    def test_age_of_majority(self):
        age_of_majority_works(self, 17)
        age_of_majority_works(self, 18)
        age_of_majority_works(self, 19)


def age_of_majority_works(test, a):
    with mock.patch('__builtin__.raw_input', side_effect=[a]):
        captured_output = StringIO.StringIO()
        sys.stdout = captured_output

        age_of_majority()
        sys.stdout = sys.__stdout__

        test.assertTrue((len(captured_output.getvalue()) > 0), msg="You did not ask anything!")

        if a > 17:

            test.assertTrue("have reached" in captured_output.getvalue(),
                            msg="The age " + str(a) + "have reached the age majority"
                                + " you output: " + captured_output.getvalue())

        else:
            test.assertTrue(("have not reached" in captured_output.getvalue()),
                            msg="You should output \"You have not reached the age majority\" to print the result."
                                " You printed: " + captured_output.getvalue())

            test.assertTrue("have not reached" in captured_output.getvalue(),
                            msg="The age " + str(a) + "have not reached the age majority"
                                + " you output: " + captured_output.getvalue())


if __name__ == '__main__':
    unittest.main()
