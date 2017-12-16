#!/usr/bin/env python2
import unittest
import io
import sys
import mock

sys.path.append('../')
import StringIO
from tmc import points
from src.Divider import divider


@points('9.0')
class DividerTestCase(unittest.TestCase):
    __qualname__ = "DividerTest"

    def test_divider(self):
        divider_works(self, 6, 2)
        divider_works(self, 3, -2)
        divider_works(self, 10, 3)


def divider_works(test, a, b):
    with mock.patch('__builtin__.raw_input', side_effect=[a, b]):
        captured_output = StringIO.StringIO()
        sys.stdout = captured_output

        divider()
        sys.stdout = sys.__stdout__

        test.assertTrue((len(captured_output.getvalue()) > 0), msg="You did not ask anything!")

        test.assertTrue(("sion:" in captured_output.getvalue()),
                        msg="You should output \"Division: RESULT\" to print the result. You printed: "
                            + captured_output.getvalue())

        test_division = captured_output.getvalue()[captured_output.getvalue().index('sion: ') + len('sion: '):]
        correct_division = float(a) / float(b)
        test.assertTrue(str(correct_division) in captured_output.getvalue(),
                        msg=str(a) + " / " + str(b) + " should be: " + str(
                            correct_division) + " you proposed: " + test_division +
                            "Did you remember to convert the values to double type?")


if __name__ == '__main__':
    unittest.main()
