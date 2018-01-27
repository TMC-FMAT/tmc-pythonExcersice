#!/usr/bin/env python2
# encoding: windows-1252


def main():
    list = []
    list.append(1)
    list.append(2)
    list.append(3)
    list.append(4)
    list.append(5)

    print 'The average is: ' + str(average(list))


# code here the method average
def average(list):
    sum = sum_array(list)
    return sum / len(list)


# copy here the method sum_array
def sum_array(list):
    return sum(list)


if __name__ == "__main__":
    main()
