#!/usr/bin/env python2
# encoding: windows-1252


def main():
    # Implement your program here. Remember to ask the input from user
    n = raw_input('Type your name: ')
    print 'Firsts three characters: ' + str(first_character(n))


def first_character(name):
    return name[0:3]


if __name__ == "__main__":
    main()
