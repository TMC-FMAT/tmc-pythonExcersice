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


@points('21')
class MainTest(unittest.TestCase):
    __qualname__ = 'MainTest'

    def test_01(self):
        leap_years = [1600, 1604, 1608, 1612, 1616, 1620, 1624, 1628, 1632, 1636, 1640, 1644, 1648, 1652]
        no_leap_years = [1601, 1605, 1609, 1613, 1615, 1621, 1623, 1627, 1631, 1635, 1641, 1643, 1649, 1653]

        for leap_year in leap_years:
            logic_works_with_leap_years(self, leap_year)

        for no_leap_year in no_leap_years:
            logic_works_with_no_leap_years(self, no_leap_year)


def logic_works_with_leap_years(test, year):
    with mock.patch('__builtin__.raw_input', side_effect=[year]):
        captured_output = StringIO.StringIO()
        sys.stdout = captured_output

        main()
        sys.stdout = sys.__stdout__

        test.assertTrue((len(captured_output.getvalue()) > 0), msg="You did not ask anything!")

        test.assertTrue(('is a leap' in captured_output.getvalue() or 'is not' in captured_output.getvalue()),
                        msg="You should output \"The year (is/is not) a leap year\" "
                            "to print the result. You printed: " + captured_output.getvalue())

        test.assertTrue('is a leap' in captured_output.getvalue(),
                        msg="The year " + str(year) + " is a leap year, you printed: " + captured_output.getvalue())


def logic_works_with_no_leap_years(test, year):
    with mock.patch('__builtin__.raw_input', side_effect=[year]):
        captured_output = StringIO.StringIO()
        sys.stdout = captured_output

        main()
        sys.stdout = sys.__stdout__

        test.assertTrue((len(captured_output.getvalue()) > 0), msg="You did not ask anything!")

        test.assertTrue(('is not a leap' in captured_output.getvalue() or 'is not' in captured_output.getvalue()),
                        msg="You should output \"The year (is/is not) a leap year\" "
                            "to print the result. You printed: " + captured_output.getvalue())

        test.assertTrue('is not a leap' in captured_output.getvalue(),
                        msg="The year " + str(year) + " is not a leap year, you printed: " + captured_output.getvalue())


if __name__ == '__main__':
    unittest.main()
