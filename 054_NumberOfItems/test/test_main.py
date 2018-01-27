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
count_items = load('src.main', 'count_items')


@points('29')
class MainTest(unittest.TestCase):
    __qualname__ = 'MainTest'

    def test_01(self):
        list = ['1', '2', '3', '4']
        self.assertTrue(count_items(list) == 4, msg='The funtion returns ' + str(count_items(list))
                                                    + ' to an array with 4 elements')

    @patch('src.main.count_items')
    def test_function_called(self, mock_to_call):
        main()
        self.assertTrue(mock_to_call.called, msg='The function count_items was not called')


if __name__ == '__main__':
    unittest.main()
