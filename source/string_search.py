#!python

import sys

def find(string, sub_string):
    count = 0

    for char in string:
        if char == sub_string[count]:
            count += 1
        else:
            count = 0

        if count == len(sub_string):
            return True

    return False


def main():
    string = sys.argv[1]
    sub_string = sys.argv[2]

    print find(string, sub_string)

if __name__ == '__main__':
    main()