#!python

import string


def decode(str_num, base):
    """
    Decode given number from given base to base 10.
    str_num -- string representation of number in given base
    base -- base of given number
    """
    assert 2 <= base <= 36

    #decimal = 0
    #for i in xrange(len(str_num)):
    #    power = len(str_num) - 1 - i
    #    decimal += int(str_num[i], base) * (base ** power)

    return int(str_num, base)

def encode(num, base):
    """
    Encode given number from base 10 to given base.
    num -- the number in base 10
    base -- base to convert to
    """
    assert 2 <= base <= 36
    encoded = []
    while num is not 0:
        remainder = num % base

        char_num = str(remainder)
        if remainder >= 10:
            char_num = chr(remainder + 87)

        encoded.insert(0, char_num)
        num = int(num / base)

    return "".join(encoded)

def convert(str_num, base1, base2):
    """
    Convert given number from base1 to base2.
    """
    assert 2 <= base1 <= 36
    assert 2 <= base2 <= 36
    decoded_num = decode(str_num, base1)
    return encode(decoded_num, base2)


def main():
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 3:
        str_num = args[0]
        base1 = int(args[1])
        base2 = int(args[2])
        result = convert(str_num, base1, base2)
        print('{} in base {} is {} in base {}'.format(str_num, base1, result, base2))
    else:
        print('Usage: {} number base1 base2'.format(sys.argv[0]))


if __name__ == '__main__':
    main()
