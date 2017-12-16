#!/usr/bin/env python2
# encoding: windows-1252
import math


def grades_and_points():
    # Implement your program here. Remember to ask the input from user
    points = raw_input('Type the points [0-100]: ')

    if int(points) > 59:
        print('Status: approved')

    else:
        print('Status: failed')


if __name__ == "__main__":
    grades_and_points()
