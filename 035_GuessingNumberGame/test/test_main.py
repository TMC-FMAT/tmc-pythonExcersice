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


@points('22')
class MainTest(unittest.TestCase):
    __qualname__ = 'MainTest'

    def test_01(self):
        logic_works_with_password(self)


def logic_works_with_password(test):
    with mock.patch('__builtin__.raw_input', side_effect=['no', 'car', 'box', 'train', 'fish', 'carrot']):
        captured_output = StringIO.StringIO()
        sys.stdout = captured_output

        main()
        sys.stdout = sys.__stdout__

        test.assertTrue((len(captured_output.getvalue()) > 0), msg="You did not ask anything!")

        test.assertTrue(('in' in captured_output.getvalue() or 'dont have' in captured_output.getvalue()),
                        msg="You should output \"You are in\" or \"You dont have access yet\" " +
                            "to print the result. You printed: " + captured_output.getvalue())

        test.assertTrue('in' in captured_output.getvalue().split('\n')[-2],
                        msg="The password carrot cant enter to the system")


if __name__ == '__main__':
    unittest.main()
