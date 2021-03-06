#!python

import sys

def find(string, sub_string):
    count = 0

    if string == sub_string:
        return True
    for char in string:
        print sub_string[count]
        if char == sub_string[count]:
            count += 1
        else:
            count = 0
            if char == sub_string[count]:
                count += 1

        if count == len(sub_string):
            return True

    return False

def find_index(string, sub_string):
    count = 0

    for i, char in enumerate(string):
        if char == sub_string[count]:
            count += 1
        else:
            count = 0
            if char == sub_string[count]:
                count += 1

        if count == len(sub_string):
            return i - (count - 1)

    return None

def main():
    string = sys.argv[1]
    sub_string = sys.argv[2]

    print find(string, sub_string)

if __name__ == '__main__':
    main()
