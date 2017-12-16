#!/usr/bin/env python2
# encoding: windows-1252


def main():
    # Implement your program here. Remember to ask the input from user
    password = "carrot"
    user_input = ""

    while user_input != password:
        print('You dont have access yet')
        user_input = raw_input('Type the password: ')

    print('Your in')


if __name__ == "__main__":
    main()
