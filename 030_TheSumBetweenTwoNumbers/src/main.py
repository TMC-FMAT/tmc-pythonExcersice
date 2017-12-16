#!/usr/bin/env python2
# encoding: windows-1252


def main():
    # Implement your program here. Remember to ask the input from user
    first = raw_input('First: ')
    last = raw_input('Last: ')
    total = 0

    while int(first) <= int(last):
        total = int(total) + int(first)
        first = int(first) + 1

    print "Sum: " + str(total)


if __name__ == "__main__":
    main()
