#!/usr/bin/env python2
# encoding: windows-1252


def adder():
    # Implement your program here. Remember to ask the input from user
    a = raw_input('Enter first number ')
    b = raw_input('Enter second number ')

    result = a + b
    toPrint = "Sum of the numbers: " + str(a) + " + " + str(b) + " = " + str(result)
    print(toPrint)


if __name__ == "__main__":
    adder()
