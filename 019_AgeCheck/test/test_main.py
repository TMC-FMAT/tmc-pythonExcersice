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

    def test_01(self):
        logic_works(self, -3)
        logic_works(self, 3)
        logic_works(self, 120)
        logic_works(self, 312)


def logic_works(test, a):
    with mock.patch('__builtin__.raw_input', side_effect=[a]):
        captured_output = StringIO.StringIO()
        sys.stdout = captured_output

        main()
        sys.stdout = sys.__stdout__

        test.assertTrue((len(captured_output.getvalue()) > 0), msg="You did not ask anything!")

        test.assertTrue(('Ok' in captured_output.getvalue() or 'mpossible' in captured_output.getvalue()),
                        msg="You should output \"Ok or Impossible\" to print the result. You printed: "
                            + captured_output.getvalue())

        if 0 <= a <= 121:
            correct_answer = "Ok"
        else:
            correct_answer = "Impossible"

        test_result = captured_output.getvalue()

        test.assertTrue(correct_answer in captured_output.getvalue(),
                        msg="A human with " + str(a) + " years should be: " + str(
                            correct_answer) + " you proposed: " + test_result)


if __name__ == '__main__':
    unittest.main()
