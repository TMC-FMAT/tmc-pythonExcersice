#!/usr/bin/env python2
# encoding: windows-1252


def main():
    list = []
    list.append('Moi')
    list.append('Ciao')
    list.append('Hello')
    print str(count_items(list))


# implement here the method countItems
def count_items(list):
    #  write your code here
    #  note that method does now print anything
    return len(list)


if __name__ == "__main__":
    main()
