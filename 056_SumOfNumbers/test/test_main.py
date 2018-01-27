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
sum_array = load('src.main', 'sum_array')


@points('29')
class MainTest(unittest.TestCase):
    __qualname__ = 'MainTest'

    def test_01(self):
        list = [1, 2, 3, 4, 5, 6]
        out = sum_array(list)
        self.assertTrue(out == sum(list), msg='The funtion returns ' + str(out)
                                                    + ' to this array: ' + str(list))

    @patch('src.main.sum_array')
    def test_function_called(self, mock_to_call):
        main()
        self.assertTrue(mock_to_call.called, msg='The function sum_array was not called')


if __name__ == '__main__':
    unittest.main()