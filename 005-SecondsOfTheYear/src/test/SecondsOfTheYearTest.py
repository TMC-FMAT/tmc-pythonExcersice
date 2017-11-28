#!/usr/bin/env python2
import unittest
import sys
sys.path.append('../')
import StringIO
from tmc import points
from src.SecondsOfTheYear import secondsOfTheYear


@points('1.0')
class SecondsOfTheYearTestCase(unittest.TestCase):
    __qualname__ = "SecondOfTheYearTest"

    def test_second_of_the_year(self):
        answer = "31536000"
        capturedOutput = StringIO.StringIO()
        sys.stdout = capturedOutput
        secondsOfTheYear()
        sys.stdout = sys.__stdout__
        self.assertTrue((answer in capturedOutput.getvalue()), msg="Printed value is not correct!")


if __name__ == '__main__':
    unittest.main()
