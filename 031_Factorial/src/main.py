#!/usr/bin/env python2
# encoding: windows-1252


def main():
    # Implement your program here. Remember to ask the input from user
    n = raw_input('Type a number: ')

    count = 1
    factorial = 1

    while count <= int(n):
        factorial = factorial * count
        count = count + 1

    print "Factorial: " + str(factorial)


if __name__ == "__main__":
    main()
