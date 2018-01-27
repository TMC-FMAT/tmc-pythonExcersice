#!/usr/bin/env python2
import unittest
import io
import sys
import mock
import StringIO
from tmc import points
from tmc.utils import load, get_stdout

sys.path.append('../')
least = load('src.main', 'least')


@points('22')
class MainTest(unittest.TestCase):
    __qualname__ = 'MainTest'

    def test_01(self):
        logic_works(self, 1, 2)

    def test_02(self):
        logic_works(self, 2, 2)

    def test_03(self):
        logic_works(self, 2, 1)


def logic_works(test, n1, n2):
    captured_output = StringIO.StringIO()
    sys.stdout = captured_output
    res = least(n1, n2)
    sys.stdout = sys.__stdout__

    if n1 <= n2:
        answer = n1
    else:
        answer = n2

    test.assertEqual(res, answer,
                    msg='Wrong answer whit ' + str(n1) + ' and ' + str(n2) +
                        ' you return: ' + str(res))


if __name__ == '__main__':
    unittest.main()
