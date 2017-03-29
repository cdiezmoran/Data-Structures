#!python

from string_search import find, find_index
import unittest

class TestStringSearch(unittest.TestCase):
    def test_find_with_sub_string_in_string(self):
        assert find('', '') == True
        assert find('Hola', 'o') == True
        assert find('Hola', 'la') == True
        assert find('Hola', 'Hol') == True
        assert find('taco cat', 'o c') == True

    def test_find_with_sub_string_not_in_string(self):
        assert find('abc', 'def') == False
        assert find('Hola', 'z') == False
        assert find('Hola', 'lo') == False
        assert find('Hola', 'Hole') == False
        assert find('taco cat', 'cat ') == False

    def test_find_index_with_sub_string_in_string(self):
        assert find_index('abc', 'a') == 0
        assert find_index('hello', 'el') == 1
        assert find_index('hello', 'lo') == 3
        assert find_index('this is a sentence', 'ten') == 13
        assert find_index('another sentence', 'other ') == 2

    def test_find_index_with_sub_string_not_in_string(self):
        assert find_index('abc', 'd') == None
        assert find_index('hello', 'ol') == None
        assert find_index('hello', 'lop') == None
        assert find_index('this is a sentence', 'tenz') == None
        assert find_index('another sentence', 'other  ') == None

if __name__ == '__main__':
    unittest.main()
