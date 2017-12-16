#!/usr/bin/env python2
# encoding: windows-1252


def main():
    # Implement your program here. Remember to ask the input from user
    user = raw_input('Type your username: ')
    password = raw_input('Type your password: ')

    if (user == 'user1' and password == 'password1') or (user == 'user2' and password == 'password2'):
        to_print = "Welcome!"
    else:
        to_print = "Invalid credentials"

    print(to_print)


if __name__ == "__main__":
    main()
