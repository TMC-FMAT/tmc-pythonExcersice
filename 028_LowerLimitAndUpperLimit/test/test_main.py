#!/usr/bin/env python2
import unittest
import io
import sys
import mock
import StringIO
from tmc import points
from tmc.utils import load, get_stdout
sys.path.append('../')
main = load('src.main', 'main')


@points('19')
class MainTest(unittest.TestCase):
    __qualname__ = 'MainTest'

    def test_01(self):
        logic_works(self, 1, 10)
        logic_works(self, 1, 50)


def logic_works(test, a, b):
    with mock.patch('__builtin__.raw_input', side_effect=[a, b]):
        captured_output = StringIO.StringIO()
        sys.stdout = captured_output

        main()
        sys.stdout = sys.__stdout__

        test.assertTrue((len(captured_output.getvalue()) > 0), msg="You did not ask anything!")

        lines = captured_output.getvalue().split('\n')
        n_lines = len(lines)

        test.assertTrue(lines[0] == str(a), msg="Your line 1 has the number " + str(lines[0]))
        test.assertTrue(lines[b-1] == str(b), msg="Your last line has the number " + str(lines[b-1]))


if __name__ == '__main__':
    unittest.main()
