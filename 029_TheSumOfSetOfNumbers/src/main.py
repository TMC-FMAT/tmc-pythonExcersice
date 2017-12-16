#!/usr/bin/env python2
# encoding: windows-1252


def main():
    # Implement your program here. Remember to ask the input from user
    n = raw_input('Until what? ')
    cont = 1
    total = 0

    while cont <= int(n):
        total = total + cont
        cont = cont + 1

    print "Sum: " + str(total)


if __name__ == "__main__":
    main()
