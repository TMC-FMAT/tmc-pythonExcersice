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


@points('29')
class MainTest(unittest.TestCase):
    __qualname__ = 'MainTest'

    def test_01(self):
        logic_works(self, 'Dakota')
        logic_works(self, '_kobe')
        logic_works(self, 'Lo')
        logic_works(self, 'L')


def logic_works(test, name):
    with mock.patch('__builtin__.raw_input', side_effect=[name]):
        captured_output = StringIO.StringIO()
        sys.stdout = captured_output
        main()
        sys.stdout = sys.__stdout__
        test.assertTrue((len(captured_output.getvalue()) > 0), msg="You did not ask anything!")

        test.assertTrue((": " in captured_output.getvalue()),
                        msg="You should output \"leter_number: letter\" to print the result. You printed: "
                            + captured_output.getvalue())
        lines = captured_output.getvalue().split('\n')

        for i in xrange(len(name)):
            letter = lines[i][lines[i].index(': ') + len(': '):]
            test.assertEqual(name[i], letter,
                             msg="The letter " + str(i+1) + " is " + name[i] + " you print: " + letter)


if __name__ == '__main__':
    unittest.main()
