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
        logic_works(self, ['hello', 'yellow', 'car', 'car'])
        logic_works(self, ['hell', 'yellow', 'car', '1', 'guess', 'hell'])
        logic_works(self, ['music', 'music'])


def logic_works(test, words):
    with mock.patch('__builtin__.raw_input', side_effect=words):
        captured_output = StringIO.StringIO()
        sys.stdout = captured_output
        main()
        sys.stdout = sys.__stdout__
        test.assertTrue((len(captured_output.getvalue()) > 0), msg="You did not ask anything!")

        test.assertTrue(("the " in captured_output.getvalue()),
                        msg="You should output \"You have the word WORD twice\" to print the result. You printed: "
                            + captured_output.getvalue())

        last_word = words[-1]
        words_duplicated = list_duplicates(words)
        test.assertTrue(len(words_duplicated) == 1, msg="Your array has more than one word duplicated")

        test.assertTrue(words_duplicated[0] == last_word, msg="The last word is not duplicated in the array")


def list_duplicates(seq):
    seen = set()
    seen_add = seen.add
    seen_twice = set(x for x in seq if x in seen or seen_add(x))
    return list(seen_twice)


if __name__ == '__main__':
    unittest.main()
