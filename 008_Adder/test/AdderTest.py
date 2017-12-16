#!/usr/bin/env python2
import unittest
import io
import sys
import mock
sys.path.append('../')
import StringIO
from tmc import points
from src.Adder import adder


@points('8.0')
class AdderTestCase(unittest.TestCase):
    __qualname__ = "AdderTest"

    def test_adder(self):
        adder_works(self, 62, 2)
        adder_works(self, -10, -5)
        adder_works(self, 0, 0)


def adder_works(test, a, b):
    with mock.patch('__builtin__.raw_input', side_effect=[a, b]):
        captured_output = StringIO.StringIO()
        sys.stdout = captured_output

        adder()
        sys.stdout = sys.__stdout__

        test.assertTrue((len(captured_output.getvalue()) > 0), msg="You did not ask anything!")

        test.assertTrue(("bers:" in captured_output.getvalue()),
                    msg="You should output \"Sum of the numbers: RESULT\" to print the result. You printed: "
                        + captured_output.getvalue())

        test_sum = captured_output.getvalue()[captured_output.getvalue().index('bers:') + len('bers: ')]
        correct_sum = a + b
        test.assertTrue(str(correct_sum) in captured_output.getvalue(), msg=str(a) + " + " + str(b) + " should be: " +
                        str(correct_sum) + " you proposed: " + test_sum)


if __name__ == '__main__':
    unittest.main()
