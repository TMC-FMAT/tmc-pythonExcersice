#!/usr/bin/env python2
# encoding: windows-1252


def main():
    # Implement your program here. Remember to ask the input from user
    year = raw_input('Type a year: ')

    if int(year) % 4 == 0:
        if int(year) % 100 != 0:
            print("The year is a leap year.")
        elif int(year) % 400 != 0:
            print("The year is not a leap year.")
        else:
            print("The year is a leap year.")
    else:
        print("The year is not a leap year.")


if __name__ == "__main__":
    main()
