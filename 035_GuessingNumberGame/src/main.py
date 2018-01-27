#!/usr/bin/env python2
# encoding: windows-1252
from random import randint


def main():
    score = 0
    usernum = 0
    random_num = randint(1, 9)

    # Program solution here. Do not touch the above lines!
    while int(usernum) != random_num:
        usernum = raw_input('Guess a number (1-9): ')

        if int(usernum) == random_num:
            print "Congratulations, your guess is correct!"
            break

        if int(usernum) > random_num:
            score = score + 1
            print "The number is lesser, guesses made: " + str(score)

        elif int(usernum) < random_num:
            score = score + 1
            print "The number is greater, guesses made: " + str(score)


if __name__ == "__main__":
    main()
