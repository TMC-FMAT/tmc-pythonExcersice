#!/usr/bin/env python2
# encoding: windows-1252


def sum_of_the_ages():
    # Implement your program here. Remember to ask the input from user
    a = raw_input('Type a number: ')
    b = raw_input('Type another number: ')

    result = max(a, b)
    to_print = "Bigger number: " + str(result)
    print(to_print)


if __name__ == "__main__":
    sum_of_the_ages()
