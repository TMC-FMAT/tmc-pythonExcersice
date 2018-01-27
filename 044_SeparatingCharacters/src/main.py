#!/usr/bin/env python2
# encoding: windows-1252


def main():
    # Implement your program here. Remember to ask the input from user
    n = raw_input('Type your name: ')

    for i in xrange(len(n)):
        print str(i+1) + ": " + n[i]


if __name__ == "__main__":
    main()
