#!/usr/bin/env python2
import unittest
import io
import sys
import mock
import StringIO
from tmc import points
from tmc.utils import load, get_stdout

sys.path.append('../')
greatest = load('src.main', 'greatest')


@points('22')
class MainTest(unittest.TestCase):
    __qualname__ = 'MainTest'

    def test_01(self):
        logic_works(self, -5, -8, -4, -4)

    def test_02(self):
        logic_works(self, 42, 5, 9, 42)

    def test_03(self):
        logic_works(self, 9, 9, 9, 9)

    def test_04(self):
        logic_works(self, 0, 0, 0, 0)

    def test_05(self):
        logic_works(self, 9, 9, 9, 9)


def logic_works(test, n1, n2, n3, answer):
    captured_output = StringIO.StringIO()
    sys.stdout = captured_output
    res = greatest(n1, n2, n3)
    sys.stdout = sys.__stdout__

    test.assertEqual(res, answer,
                     msg='Greatest of ' + str(n1) + ", " + str(n2) + ", " + str(n3) + ' is ' + str(answer) +
                     ' you return: ' + str(res))


if __name__ == '__main__':
    unittest.main()
