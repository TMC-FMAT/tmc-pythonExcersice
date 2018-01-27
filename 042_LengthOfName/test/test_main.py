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
first_character = load('src.first_character', 'first_character')
main = load('src.main', 'main')


@points('29')
class MainTest(unittest.TestCase):
    __qualname__ = 'MainTest'

    def test_01(self):
        logic_works(self, 'Dakota', 6)
        logic_works(self, 'Daniela', 7)
        logic_works(self, '', 0)


def logic_works(test, name, answer):
    with mock.patch('__builtin__.raw_input', side_effect=[name]):
        captured_output = StringIO.StringIO()
        sys.stdout = captured_output
        main()
        sys.stdout = sys.__stdout__
        test.assertTrue((len(captured_output.getvalue()) > 0), msg="You did not ask anything!")

        test.assertTrue(("characters: " in captured_output.getvalue()),
                        msg="You should output \"Number of characters: ANSWER\" to print the result. You printed: "
                            + captured_output.getvalue())

        test_result = captured_output.getvalue()[captured_output.getvalue().index('ters: ') + len('ters: '):]

        test.assertEqual(int(test_result), answer,
                        msg="The answer is: '" + str(answer) + "' you proposed: '" + str(test_result) + "'")


if __name__ == '__main__':
    unittest.main()
