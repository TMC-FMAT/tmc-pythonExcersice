#!/usr/bin/env python2
# encoding: windows-1252


def even_or_odd():
    # Implement your program here. Remember to ask the input from user
    number = raw_input('Type a number: ')

    if int(number) % 2 == 0:
        result = 'Number ' + str(number) + " is even"

    else:
        result = 'Number ' + str(number) + " is odd"

    print(result)


if __name__ == "__main__":
    even_or_odd()
