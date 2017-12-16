#!/usr/bin/env python2
# encoding: windows-1252


def positive_value():
    # Implement your program here. Remember to ask the input from user
    a = raw_input('Type a number: ')

    if int(a) > 0:
        result = "The number is positive"
    else:
        result = "The number is negative"

    print(result)


if __name__ == "__main__":
    positive_value()
