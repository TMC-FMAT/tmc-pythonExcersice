#!/usr/bin/env python2
# encoding: windows-1252
import math


def main():
    # Implement your program here. Remember to ask the input from user
    n = raw_input('Type a number: ')

    count = 1
    result = 0

    while count <= int(n):
        result = result + count*count
        count = count + 1

    print "Result: " + str(result)


if __name__ == "__main__":
    main()
