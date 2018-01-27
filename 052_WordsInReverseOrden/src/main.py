#!/usr/bin/env python2
# encoding: windows-1252


def main():
    # Implement your program here. Remember to ask the input from user
    words = []
    while True:
        word = raw_input('Type a word: ')
        if word == '':
            break
        words.append(word)

    print 'You typed the following words: '

    for word in words[::-1]:
        print word


if __name__ == "__main__":
    main()
