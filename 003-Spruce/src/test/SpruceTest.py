#!/usr/bin/env python2
import unittest
import sys
sys.path.append('../')
import StringIO
from tmc import points
from src.Spruce import spruce


@points('1.0')


class SpruceTestCase(unittest.TestCase):
    __qualname__ = "SpruceTest"

    def test_spruce(self):
        awaitedValue = "    *\n" + "   ***\n" + "  *****\n" + " *******\n" + "*********\n" + "    *\n"
        capturedOutput = StringIO.StringIO()
        sys.stdout = capturedOutput
        spruce()
        sys.stdout = sys.__stdout__
        self.assertEqual(capturedOutput.getvalue(), awaitedValue, msg="you need print a spruce!")


if __name__ == '__main__':
    unittest.main()
