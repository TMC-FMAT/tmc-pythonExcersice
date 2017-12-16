#!/usr/bin/env python2
# encoding: windows-1252


def main():
    # Implement your program here. Remember to ask the input from user
    age = raw_input('How old are you: ')

    if 0 <= int(age) <= 121:
        to_print = "Ok"
    else:
        to_print = "Impossible"

    print(to_print)


if __name__ == "__main__":
    main()
