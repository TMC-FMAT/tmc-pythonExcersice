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
average = load('src.main', 'average')


@points('29')
class MainTest(unittest.TestCase):
    __qualname__ = 'MainTest'

    def test_01(self):
        list = [1, 2, 3, 4, 5, 6]
        out = average(list)
        answer = reduce(lambda x, y: x + y, list) / len(list)
        self.assertTrue(out == answer, msg='The funtion returns ' + str(out)
                                                    + ' to this array: ' + str(list) +
                                              '\n correct answer: ' + str(answer))

    @patch('src.main.sum_array')
    def test_sum_called(self, mock_to_call):
        average([1, 2])
        self.assertTrue(mock_to_call.called, msg='The function sum_array was not called')

    @patch('src.main.average')
    def test_average_called(self, mock_to_call):
        main()
        self.assertTrue(mock_to_call.called, msg='The function average was not called')


if __name__ == '__main__':
    unittest.main()