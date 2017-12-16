#!/usr/bin/env python2
# encoding: windows-1252


def greater_number():
    # Implement your program here. Remember to ask the input from user
    a = raw_input('Type a number: ')
    b = raw_input('Type another number: ')

    if int(a) == int(b):
        result = 'The numbers are equal'

    elif int(a) > int(b):
        result = 'Greater number: ' + str(a)
    else:
        result = 'Greater number: ' + str(b)

    print(result)


if __name__ == "__main__":
    greater_number()
