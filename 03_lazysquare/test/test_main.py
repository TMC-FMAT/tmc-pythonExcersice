import unittest
import io
import contextlib
from unittest.mock import patch

from tmc import points

from tmc.utils import load, get_stdout
main = load('src.main', 'main')


@points('1.3')
class MainTest(unittest.TestCase):

    def test_00_something_is_printed(self):
        self.longMessage = False
        main()
        printed = get_stdout()
        if not printed:
            self.fail('Et tulostanut mitään!')

    def test_01_prints_correct_first_row(self):
        self.longMessage = False
        main()
        printed = get_stdout()
        line = printed.split('\n')[0].strip()
        self.assertEqual(line, '* * * * *',msg='Et tulostanut neliötä oikein')

    def test_02_prints_correct_second_row(self):
        self.longMessage = False
        main()
        printed = get_stdout()
        line = printed.split('\n')[1].strip()
        self.assertEqual(line, '* * * * *',msg='Et tulostanut neliötä oikein')

    def test_03_prints_correct_third_row(self):
        self.longMessage = False
        main()
        printed = get_stdout()
        line = printed.split('\n')[2].strip()
        self.assertEqual(line, '* * * * *',msg='Et tulostanut neliötä oikein')

    def test_04_prints_correct_fourth_row(self):
        self.longMessage = False
        main()
        printed = get_stdout()
        line = printed.split('\n')[3].strip()
        self.assertEqual(line, '* * * * *',msg='Et tulostanut neliötä oikein')

    def test_05_prints_correct_fifth_row(self):
        self.longMessage = False
        main()
        printed = get_stdout()
        line = printed.split('\n')[4].strip()
        self.assertEqual(line, '* * * * *',msg='Et tulostanut neliötä oikein')
