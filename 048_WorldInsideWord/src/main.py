#!/usr/bin/env python2
# encoding: windows-1252


def main():
    # Implement your program here. Remember to ask the input from user
    first = raw_input('Type the first word: ')
    second = raw_input('Type the second word: ')

    if first in second:
        print 'The word ' + first + ' is found in the word ' + second
    else:
        print 'The word ' + first + ' is not found in the word ' + second


if __name__ == "__main__":
    main()
