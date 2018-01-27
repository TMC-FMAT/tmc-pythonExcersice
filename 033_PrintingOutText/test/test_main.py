#!/usr/bin/env python2
import unittest
import io
import sys
import mock
import StringIO
from tmc import points
from tmc.utils import load, get_stdout

sys.path.append('../')
print_text = load('src.main', 'main')


@points('25')
class MainTest(unittest.TestCase):
    __qualname__ = 'MainTest'

    def test_01(self):
        logic_works(self)


def logic_works(test):
    captured_output = StringIO.StringIO()
    sys.stdout = captured_output

    try:
        print_text()

    except NameError:
        test.assertTrue(False, msg="Your code does not has print_message() function")

    sys.stdout = sys.__stdout__

    test.assertTrue((len(captured_output.getvalue()) > 0), msg="You did not print anything!")

    test.assertTrue(('Hello' in captured_output.getvalue()),
                    msg="Hello from the function to print the result. You printed: "
                        + captured_output.getvalue())


if __name__ == '__main__':
    unittest.main()
