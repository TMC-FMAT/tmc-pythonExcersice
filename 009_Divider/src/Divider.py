#!/usr/bin/env python2
# encoding: windows-1252


def divider():
    # Implement your program here. Remember to ask the input from user
    a = raw_input('Enter first number: ')
    b = raw_input('Enter second number: ')

    result = float(a) / float(b)
    to_print = "Division: " + str(result)
    print(to_print)


if __name__ == "__main__":
    divider()
