#!/usr/bin/env python2
import unittest
import sys

sys.path.append('../')
import StringIO
from tmc import points
from src.HelloWorld import helloWorld


@points('1.0')
class HelloWorldTestCase(unittest.TestCase):
    __qualname__ = "HelloWorldTest"

    def test_helloWorld(self):
        awaitedValue = "Hello World!\n"
        capturedOutput = StringIO.StringIO()
        sys.stdout = capturedOutput
        helloWorld()
        sys.stdout = sys.__stdout__
        self.assertEqual(capturedOutput.getvalue(), awaitedValue, msg="you need print \"Hello World!\"")


if __name__ == '__main__':
    unittest.main()
