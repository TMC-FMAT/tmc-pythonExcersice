#!/usr/bin/env python2
# encoding: windows-1252


# implement here again the method of exercise 36
def sum_numbers(number1, number2, number3, number4):
    total = number1 + number2 + number3 + number4
    return total


def average(number1, number2, number3, number4):
    # write program code here
    # do not print anything inside the method
    # method needs a return in the end

    total = sum_numbers(number1, number2, number3, number4) / 4.0
    return total


if __name__ == "__main__":
    result = average(20, 9, 1, 13)
    print "Average: " + str(result)
