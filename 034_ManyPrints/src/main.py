#!/usr/bin/env python2
# encoding: windows-1252


def main():
    # Implement your program here. Remember to ask the input from user
    number = raw_input('How many times? ')
    cont = 1

    while cont <= int(number):
        print_text()
        cont = cont + 1


def print_text():
    print('Hello from the function')


if __name__ == "__main__":
    main()
