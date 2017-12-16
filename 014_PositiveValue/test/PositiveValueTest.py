#!/usr/bin/env python2
import unittest
import io
import sys
import mock

sys.path.append('../')
import StringIO
from tmc import points
from src.PositiveValue import positive_value


@points('9.0')
class PostiveValueTestCase(unittest.TestCase):
    __qualname__ = "PositiveValueTest"

    def test_positive_value(self):
        positive_value_works(self, 6)
        positive_value_works(self, -6)


def positive_value_works(test, a):
    with mock.patch('__builtin__.raw_input', side_effect=[a]):
        captured_output = StringIO.StringIO()
        sys.stdout = captured_output

        positive_value()
        sys.stdout = sys.__stdout__

        test.assertTrue((len(captured_output.getvalue()) > 0), msg="You did not ask anything!")

        test.assertTrue(("number is" in captured_output.getvalue()),
                        msg="You should output \"The number is positive/negative\" to print the result. You printed: "
                            + captured_output.getvalue())
        if a > 0:
            find = 'positive'
        else:
            find = 'negative'

        test_result = captured_output.getvalue()[captured_output.getvalue().index('is ') + len('is '):]

        test.assertTrue(find in captured_output.getvalue(),
                        msg='The number is ' + find + " you proposed: " + test_result)


if __name__ == '__main__':
    unittest.main()
