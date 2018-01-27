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
print_text = load('src.main', 'print_text')


@points('23')
class MainTest(unittest.TestCase):
    __qualname__ = 'MainTest'

    def test_01(self):
        logic_works(self, 5)


def logic_works(test, a):
    with mock.patch('__builtin__.raw_input', side_effect=[a]):
        captured_output = StringIO.StringIO()
        sys.stdout = captured_output

        main()
        sys.stdout = sys.__stdout__

        test.assertTrue((len(captured_output.getvalue()) > 0), msg="You did not print anything!")

        try:
            print_text()

        except NameError:
            test.assertTrue(False, msg="Your code does not has print_message() function")

        lines = captured_output.getvalue().split('\n')
        n_lines = len(lines) - 1

        test.assertTrue(('ello' in lines[0]),
                        msg="You should output \"Hello from the function\" "
                            " You printed: " + lines[0])

        test.assertTrue(n_lines == a, msg="You print a incorrect numbers of lines for " + str(a) + " iterations " +
                                          "you printed " + str(n_lines) + " lines")


if __name__ == '__main__':
    unittest.main()
