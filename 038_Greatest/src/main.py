#!/usr/bin/env python2
# encoding: windows-1252


def greatest(number1, number2, number3):
    # write program code here
    # do not print anything inside the method
    # method needs a return in the end

    if number1 >= number2 and number1 >= number3:
        return number1
    elif number2 >= number3 and number2 >= number1:
        return number2
    else:
        return number3


if __name__ == "__main__":
    result = greatest(8, 17, 10)
    print "Greatest: " + str(result)
