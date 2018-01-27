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
reverse = load('src.main', 'reverse')


@points('29')
class MainTest(unittest.TestCase):
    __qualname__ = 'MainTest'

    def test_01(self):
        # logic_works(self, ['hello', 'yellow', 'car', ''])
        logic_works(self, ['a', 'b', 'car', 'd', 'ernest', ''])
        logic_works(self, ['music', ''])


def logic_works(test, words):
    with mock.patch('__builtin__.raw_input', side_effect=words):
        captured_output = StringIO.StringIO()
        sys.stdout = captured_output
        main()
        sys.stdout = sys.__stdout__
        test.assertTrue((len(captured_output.getvalue()) > 0), msg="You did not ask anything!")

        test.assertTrue(("words: " in captured_output.getvalue()),
                        msg="You should output your result as follows:\nYou typed the following words:" +
                            "\nWORD1 \nWORD2 \n..." + "\nYou printed: " + captured_output.getvalue())

        lines = captured_output.getvalue().split('\n')
        words.sort()
        words.remove('')

        for i in xrange(len(words)):
            test.assertEqual(words[i], lines[i+1].strip(),
                             msg="The word " + str(i+1) + " is " + words[i] + " you print: " + lines[i+1])


if __name__ == '__main__':
    unittest.main()
