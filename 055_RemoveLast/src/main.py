#!/usr/bin/env python2
# encoding: windows-1252


def main():
    list = []
    list.append('Moi')
    list.append('Ciao')
    list.append('Hello')
    list.append('Brian')
    print 'Persons ' + str(remove_last(list))


# implement here the method remove_last
def remove_last(list):
    #  write your code here
    #  note that method does now print anything
    return list[:-1]


if __name__ == "__main__":
    main()
