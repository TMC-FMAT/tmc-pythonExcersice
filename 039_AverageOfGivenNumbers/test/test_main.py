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
average = load('src.main', 'average')
sum_of_numbers = load('src.main', 'sum_of_numbers')


@points('22')
class MainTest(unittest.TestCase):
    __qualname__ = 'MainTest'

    def test_01(self):
        logic_works(self, -5, -8, -4, 5, -3)

    def test_02(self):
        logic_works(self, 42, 5, 9, 70, 31.5)

    def test_03(self):
        logic_works(self, 9, 9, 9, 9, 9)

    def test_04(self):
        logic_works(self, 0, 0, 0, 0, 0)

    @patch('src.main.sum_numbers')
    def test_sum_called(self, mock):
        average(1, 2, 3, 4)
        self.assertTrue(mock.called, msg='The function sum_numbers was not called in average()')


def logic_works(test, n1, n2, n3, n4, answer):
    captured_output = StringIO.StringIO()
    sys.stdout = captured_output
    res = average(n1, n2, n3, n4)
    sys.stdout = sys.__stdout__

    test.assertEqual(res, answer,
                     msg='Average of ' + str(n1) + ", " + str(n2) + ", " + str(n3) + ", " + str(n4)
                         + ' is ' + str(answer) + ' you return: ' + str(res))


if __name__ == '__main__':
    unittest.main()
