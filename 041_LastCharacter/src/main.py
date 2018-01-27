#!/usr/bin/env python2
# encoding: windows-1252


def main():
    # Implement your program here. Remember to ask the input from user
    n = raw_input('Type your name: ')
    print 'Last character: ' + str(last_character(n))


def last_character(name):
    return name[-1]


if __name__ == "__main__":
    main()
