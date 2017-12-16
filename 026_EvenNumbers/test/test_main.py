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


@points('25')
class MainTest(unittest.TestCase):
    __qualname__ = 'MainTest'

    def test_01(self):
        logic_works(self)


def logic_works(test):
    captured_output = StringIO.StringIO()
    sys.stdout = captured_output
    main()
    sys.stdout = sys.__stdout__

    lines = captured_output.getvalue().split('\n')
    n_lines = len(lines)

    test.assertTrue(n_lines >= 50,  msg="You print less than 100 lines, you print " + str(n_lines) + " lines")
    test.assertTrue(lines[0] == "2",  msg="Your line 1 has the number " + str(lines[0]))
    test.assertTrue(lines[24] == "50",  msg="Your line 25 has the number " + str(lines[25]))
    test.assertTrue(lines[49] == "100",  msg="Your last line has the number " + str(lines[49]))


if __name__ == '__main__':
    unittest.main()
