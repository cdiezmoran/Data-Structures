#!python

# Hint: use string.ascii_letters (all letters in ASCII character set)
import string
import re


def is_palindrome(text):
    """A string of characters is a palindrome if it reads the same forwards and
    backwards, ignoring punctuation, whitespace, and letter casing"""
    # implement is_palindrome_iterative and is_palindrome_recursive below, then
    # change this to call your implementation to verify it passes all tests
    assert isinstance(text, str)
    return is_palindrome_recursive(text)
    # return is_palindrome_recursive(text)

# This function looks for pairs of letters and if those pairs count are equal
# to the length of the string / 2 then it is a palindrome and returns true
def is_palindrome_iterative(text):
    # Remove spaces and special characters
    text = re.sub('[^A-Za-z0-9]+', '', text.lower())
    return text == text[::-1]

def is_perm_palindrome_iterative(text):
    text = re.sub('[^A-Za-z0-9]+', '', text.lower())
    unique_letters = {}
    for letter in text:
        if letter in unique_letters:
            # If letter has a pair already
            if unique_letters[letter] == 2:
                count = 1
                entry = letter + str(count)
                # Look for the next available pair or create one (i.e. for a then "a1", "a2" ...)
                while entry in unique_letters and unique_letters[entry] == 2:
                    count += 1
                    entry = letter + str(count)
                # Next entry is in unique_letters but does not have a pair
                if entry in unique_letters:
                    unique_letters[entry] += 1
                # Next entry is not in unique_letters
                else:
                    unique_letters[entry] = 1
            # Letter is already in unique_letters but does not have a pair
            else:
                unique_letters[letter] += 1
        # Letter is not in unique_letters
        else:
            unique_letters[letter] = 1

    half_len = len(text) / 2

    # If text len is even then it must be equal
    if len(text) % 2 == 0:
        return half_len == len(unique_letters)

    # If text len is odd then we have to add 1 to it and compare (round up)
    return (half_len + 1) == len(unique_letters)

def is_palindrome_recursive(text, left=None, right=None):
    # TODO: implement the is_palindrome function recursively here
    if left is None and right is None:
        text = re.sub('[^A-Za-z0-9]+', '', text.lower())
        left = 0
        right = len(text) - 1

    if left >= right:
        return True

    if text[left] == text[right]:
        return is_palindrome_recursive(text, (left + 1), (right - 1))

    return False

def main():
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) > 0:
        for arg in args:
            is_pal = is_palindrome(arg)
            result = 'PASS' if is_pal else 'FAIL'
            str_not = 'a' if is_pal else 'not a'
            print('{}: {} is {} palindrome'.format(result, repr(arg), str_not))
    else:
        print('Usage: {} string1 string2 ... stringN'.format(sys.argv[0]))
        print('  checks if each argument given is a palindrome')


if __name__ == '__main__':
    main()
