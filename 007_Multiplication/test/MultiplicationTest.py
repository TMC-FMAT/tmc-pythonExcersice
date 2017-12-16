#!/usr/bin/env python2
import unittest
import sys
import re
sys.path.append('../')
import StringIO
from tmc import points
from src.Multiplication import multiplication


@points('7.0')
class MultiplicationTestCase(unittest.TestCase):
    __qualname__ = "MultiplicationTest"

    def test_multiplication(self):
        capturedOutput = StringIO.StringIO()
        sys.stdout = capturedOutput
        multiplication()
        sys.stdout = sys.__stdout__

        self.assertTrue((len(capturedOutput.getvalue()) > 0), msg="You did not print anything!")

        match = re.match(r'(?s).*?(\d+)\s*\*\s*(\d+)\s*=\s*(\d+).*', capturedOutput.getvalue())
        self.assertTrue(match, msg="Your output should be of the form 'X * Y = Z' for some integers X, Y and Z. "
                                      "Now it was: " + capturedOutput.getvalue())

        textA = match.group(1)
        textB = match.group(2)
        textC = match.group(3)

        a = int(textA)
        b = int(textB)
        c = int(textC)

        self.assertEqual(a*b, c, msg="Your program claims that "+str(a)+" + "+str(b)+" = " +
                                     str(c)+" , but that is not true!")


if __name__ == '__main__':
    unittest.main()
