#!/usr/bin/env python2
# encoding: windows-1252


def main():
    # Implement your program here. Remember to ask the input from user
    n = raw_input('Type your text: ')
    print 'Reverse text: ' + str(reverse(n))


def reverse(text):
    #  write your code here
    #  note that method does now print anything, it RETURNS the reversed string
    return text[::-1]


if __name__ == "__main__":
    main()
