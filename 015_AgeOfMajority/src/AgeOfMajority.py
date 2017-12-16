#!/usr/bin/env python2
# encoding: windows-1252


def age_of_majority():
    # Implement your program here. Remember to ask the input from user
    age = raw_input('How old are you? ')

    if int(age) > 17:
        result = 'You have reached the age of majority'
    else:
        result = 'You have not reached the age of majority'

    print(result)


if __name__ == "__main__":
    age_of_majority()
