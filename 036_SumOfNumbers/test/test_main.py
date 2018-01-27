#!/usr/bin/env python2
import unittest
import io
import sys
import mock
import StringIO
from tmc import points
from tmc.utils import load, get_stdout

sys.path.append('../')
sum_numbers = load('src.main', 'sum_numbers')


@points('22')
class MainTest(unittest.TestCase):
    __qualname__ = 'MainTest'

    def test_01(self):
        logic_works(self, 1, 2, 3, 4, 5)

    def test_02(self):
        logic_works(self, 0, 0, 0, 0, 0)

    def test_03(self):
        logic_works(self, 0, 0, 0, 0, sys.maxint)


def logic_works(test, n1, n2, n3, n4, n5):
    captured_output = StringIO.StringIO()
    sys.stdout = captured_output
    res = sum_numbers(n1, n2, n3, n4, n5)
    sys.stdout = sys.__stdout__

    answer = n1 + n2 + n3 + n4 + n5
    test.assertEqual(res, answer,
                    msg='The sum of ' + str(n1) + ' + ' + str(n2) + ' + ' + str(n3) +
                        ' + ' + str(n4) + ' + ' + str(n5) + ' should be : ' +
                        str(answer) + " Now it was: " + captured_output.getvalue())


if __name__ == '__main__':
    unittest.main()
