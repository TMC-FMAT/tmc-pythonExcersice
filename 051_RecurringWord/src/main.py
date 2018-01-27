#!/usr/bin/env python2
# encoding: windows-1252


def main():
    # Implement your program here. Remember to ask the input from user
    words = []
    while True:
        word = raw_input('Type a word: ')
        if word in words:
            break
        words.append(word)

    print 'You have the word ' + word + ' twice'


if __name__ == "__main__":
    main()
