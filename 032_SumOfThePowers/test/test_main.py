#!/usr/bin/env python2
import unittest
import io
import sys
import mock
import StringIO
from tmc import points
from tmc.utils import load, get_stdout
sys.path.append('../')
main = load('src.main', 'main')


@points('30')
class MainTest(unittest.TestCase):
    __qualname__ = 'MainTest'

    def test_01(self):
        with mock.patch('__builtin__.raw_input', side_effect=[2]):
            captured_output = StringIO.StringIO()
            sys.stdout = captured_output

            main()
            sys.stdout = sys.__stdout__

            self.assertTrue((len(captured_output.getvalue()) > 0), msg="You did not ask anything!")

            self.assertTrue(("sult: " in captured_output.getvalue()),
                            msg="You should output \"Result: RESULT\" to print the result. You printed: "
                                + captured_output.getvalue())

            test_result = captured_output.getvalue()[captured_output.getvalue().index('sult: ') + len('sult: '):]
            correct_answer = 5
            self.assertTrue(str(correct_answer) in captured_output.getvalue(),
                            msg="The result with input 2 is: " + str(
                                correct_answer) + " you proposed: " + test_result)

    def test_02(self):
        with mock.patch('__builtin__.raw_input', side_effect=[5]):
            captured_output = StringIO.StringIO()
            sys.stdout = captured_output

            main()
            sys.stdout = sys.__stdout__

            self.assertTrue((len(captured_output.getvalue()) > 0), msg="You did not ask anything!")

            self.assertTrue(("sult: " in captured_output.getvalue()),
                            msg="You should output \"Result: RESULT\" to print the result. You printed: "
                                + captured_output.getvalue())

            test_result = captured_output.getvalue()[captured_output.getvalue().index('sult: ') + len('sult: '):]
            correct_answer = 55
            self.assertTrue(str(correct_answer) in captured_output.getvalue(),
                            msg="The result with 5 is: " + str(
                                correct_answer) + " you proposed: " + test_result)


if __name__ == '__main__':
    unittest.main()
