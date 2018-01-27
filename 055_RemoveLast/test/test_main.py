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
remove_last = load('src.main', 'remove_last')


@points('29')
class MainTest(unittest.TestCase):
    __qualname__ = 'MainTest'

    def test_01(self):
        list = ['1', '2', '3', '4']
        out = remove_last(list)
        self.assertTrue(out == list[:-1], msg='The funtion returns ' + str(out)
                                                    + ' to an array with 4 elements')

    @patch('src.main.remove_last')
    def test_function_called(self, mock_to_call):
        main()
        self.assertTrue(mock_to_call.called, msg='The function remove_last was not called')


if __name__ == '__main__':
    unittest.main()

