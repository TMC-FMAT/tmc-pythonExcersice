#!/usr/bin/env python2
# encoding: windows-1252


def main():
    # Implement your program here. Remember to ask the input from user
    n = raw_input('Type your name: ')
    print 'Number of characters: ' + str(calculate_characters(n))


def calculate_characters(name):
    return len(name)


if __name__ == "__main__":
    main()
