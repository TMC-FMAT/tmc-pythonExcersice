#!/usr/bin/env python2
# encoding: windows-1252
from random import randint


def main():
    print sum_of_numbers(1, 2, 3, 4, 5)


def sum_of_numbers(number1, number2, number3, number4, number5):
    total = number1 + number2 + number3 + number4 + number5
    return total


if __name__ == "__main__":
    main()

