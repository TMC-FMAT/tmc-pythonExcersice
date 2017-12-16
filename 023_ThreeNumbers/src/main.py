#!/usr/bin/env python2
# encoding: windows-1252


def main():
    # Implement your program here. Remember to ask the input from user
    sum = 0
    read = 0  #store numbers read form user in this variable

    read = raw_input('Type the first number: ')
    sum += int(read)

    read = raw_input('Type the second number: ')
    sum += int(read)

    read = raw_input('Type the third number: ')
    sum += int(read)

    print('Sum: ' + str(sum))


if __name__ == "__main__":
    main()
