#!/usr/bin/env python2
# encoding: windows-1252


def main():
    # Implement your program here. Remember to ask the input from user
    n = raw_input('Type a word: ')
    end_part = raw_input('Length of the end part: ')
    print 'End part: ' + n[-int(end_part):]


if __name__ == "__main__":
    main()
