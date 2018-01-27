#!/usr/bin/env python2
import unittest
import io
import sys
import mock
import StringIO
from tmc import points
from tmc.utils import load, get_stdout
from mock import patch
sys.path.append('../')
main = load('src.main', 'main')


@points('29')
class MainTest(unittest.TestCase):
    __qualname__ = 'MainTest'

    def test_01(self):
        logic_works(self, 'Dakota', 3)
        logic_works(self, '_kobe', 2)
        logic_works(self, 'Logan', -1)


def logic_works(test, name, length):
    with mock.patch('__builtin__.raw_input', side_effect=[name, length]):
        captured_output = StringIO.StringIO()
        sys.stdout = captured_output
        main()
        sys.stdout = sys.__stdout__
        test.assertTrue((len(captured_output.getvalue()) > 0), msg="You did not ask anything!")

        test.assertTrue(("part: " in captured_output.getvalue()),
                        msg="You should output \"End part: ANSWER\" to print the result. You printed: "
                            + captured_output.getvalue())

        test_result = captured_output.getvalue()[captured_output.getvalue().index(': ') + len(': '):]

        test.assertEqual(test_result.strip(), name[-length:],
                        msg="The answer is: '" + name[:length] + "' you proposed: '" + test_result + "'")


if __name__ == '__main__':
    unittest.main()
