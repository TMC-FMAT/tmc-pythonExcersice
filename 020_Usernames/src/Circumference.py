#!/usr/bin/env python2
# encoding: windows-1252
import math


def circumference():
    # Implement your program here. Remember to ask the input from user
    radius = raw_input('Type the radius: ')
    result = float(radius) * 2 * math.pi
    to_print = "Circumference: " + str(result)
    print(to_print)


if __name__ == "__main__":
    circumference()
