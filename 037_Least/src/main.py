#!/usr/bin/env python2
# encoding: windows-1252


def least(number1, number2):
    # write program code here
    # do not print anything inside the method
    # method needs a return in the end

    if number1 <= number2:
        return number1
    else:
        return number2


if __name__ == "__main__":
    result = least(8, 7)
    print "Least: " + str(result)

