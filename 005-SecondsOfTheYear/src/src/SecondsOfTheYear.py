#!/usr/bin/env python2
# encoding: windows-1252


def secondsOfTheYear():
    # In below an incomplete version of the program. Please complete it!

    daysInYear = 365
    hoursInDay = 24
    minutesInHour = 60
    secondsInMinute = 60

    secondsInYear = daysInYear * hoursInDay * minutesInHour * secondsInMinute

    print("There are " + str(secondsInYear) + " seconds in a year");


if __name__ == "__main__":
    secondsOfTheYear()
