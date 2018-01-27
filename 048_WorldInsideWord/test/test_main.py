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
        logic_works(self, 'kota', 'Dakota')
        logic_works(self, 'test', 'tester')
        logic_works(self, 'No', 'Logan')


def logic_works(test, word1, word2):
    with mock.patch('__builtin__.raw_input', side_effect=[word1, word2]):
        captured_output = StringIO.StringIO()
        sys.stdout = captured_output
        main()
        sys.stdout = sys.__stdout__
        test.assertTrue((len(captured_output.getvalue()) > 0), msg="You did not ask anything!")

        test.assertTrue(("is not found" in captured_output.getvalue() or "is found" in captured_output.getvalue()),
                        msg="You should output \"The word WORD1 (is found/is not found) in WORD2\" to print the result."
                            + "You printed: " + captured_output.getvalue())

        if word1 in word2:
            test.assertTrue('is found' in captured_output.getvalue(),
                            msg="The " + word2 + " is found in " + word1)

        if word1 not in word2:
            test.assertTrue('is not found' in captured_output.getvalue(),
                            msg="The " + word2 + " is not found in " + word1)


if __name__ == '__main__':
    unittest.main()
