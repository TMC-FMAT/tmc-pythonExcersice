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


@points('19')
class MainTest(unittest.TestCase):
    __qualname__ = 'MainTest'

    username1 = 'user1'
    password1 = 'password1'

    username2 = 'user2'
    password2 = 'password2'

    def test_01(self):
        logic_works(self, MainTest.username1, MainTest.password1)
        logic_works(self, MainTest.username2, MainTest.password2)
        logic_works(self, MainTest.username1, MainTest.password2)


def logic_works(test, user, password):
    with mock.patch('__builtin__.raw_input', side_effect=[user, password]):
        captured_output = StringIO.StringIO()
        sys.stdout = captured_output

        main()
        sys.stdout = sys.__stdout__

        test.assertTrue((len(captured_output.getvalue()) > 0), msg="You did not ask anything!")

        test.assertTrue(('come' in captured_output.getvalue() or 'nvalid' in captured_output.getvalue()),
                        msg="You should output \"Welcome\" or \"Invalid credentials\" "
                            "to print the result. You printed: " + captured_output.getvalue())

        if (user == MainTest.username1 and password == MainTest.password1) or\
                (user == MainTest.username2 and password == MainTest.password2):
            correct_answer = "Welcome"
        else:
            correct_answer = "Invalid credentials"

        test_result = captured_output.getvalue()

        test.assertTrue(correct_answer in test_result,
                        msg="The user: " + user + " with the password: " + password +
                            " should print: " + correct_answer + " you proposed: " + test_result)


if __name__ == '__main__':
    unittest.main()
