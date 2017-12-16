#!/usr/bin/env python2
# encoding: windows-1252


def main():
    # Implement your program here. Remember to ask the input from user
    number = raw_input('Up to what number? ')
    cont = 1

    while cont <= int(number):
        print cont
        cont = cont + 1


if __name__ == "__main__":
    main()
