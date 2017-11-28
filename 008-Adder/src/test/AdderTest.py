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
        adder_works(self, 1, 2)


def adder_works(test, a, b):
    with mock.patch('__builtin__.raw_input', side_effect=[a, b]):
        captured_output = StringIO.StringIO()
        sys.stdout = captured_output

        adder()
        sys.stdout = sys.__stdout__

        test.assertTrue((len(captured_output.getvalue()) > 0), msg="You did not ask anything!")

        test.assertTrue((":" in captured_output.getvalue()),
                    msg="You should output \":\" when prompting user for input. You printed: "
                        + captured_output.getvalue())

        test.assertTrue(0, captured_output.getvalue())


if __name__ == '__main__':
    unittest.main()
