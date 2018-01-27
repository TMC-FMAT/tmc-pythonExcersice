#!/usr/bin/env python2
# encoding: windows-1252


def main():
    list = []
    list.append(1)
    list.append(2)
    list.append(3)
    list.append(4)
    list.append(5)

    print 'The sum: ' + str(sum_array(list))


# implement here the method sum_array
def sum_array(list):
    #  write your code here
    #  note that method does now print anything
    return sum(list)


if __name__ == "__main__":
    main()
