#!python

from hashset import HashSet
import unittest


class HashSetTest(unittest.TestCase):

    def test_init(self):
        elements = ["hola", "adios", "test", "test"]
        hs = HashSet(elements)
        assert hs.size == 3

    def test_add(self):
        elements = ["hola", "adios", "test", "test"]
        hs = HashSet(elements)
        hs.add("annie")
        assert hs.size == 4
        assert hs.contains("annie") == True
        hs.add("hola")
        assert hs.size == 4
        assert hs.contains("hola") == True

    def test_remove(self):
        elements = ["hola", "adios", "test", "test", "annie"]
        hs = HashSet(elements)
        assert hs.contains("annie") == True
        hs.remove("annie")
        assert hs.contains("annie") == False
        with self.assertRaises(ValueError):
            hs.remove("pamis")  # Element does not exist

    def test_union(self):
        elements1 = ["hola", "adios", "test", "test", "annie"]
        elements2 = ["pamis", "blah", "other", "test", "hola"]
        hs = HashSet(elements1)
        other_hs = HashSet(elements2)

        union = hs.union(other_hs)

        assert union.contains("hola") == True
        assert union.contains("adios") == True
        assert union.contains("test") == True
        assert union.contains("annie") == True
        assert union.contains("pamis") == True
        assert union.contains("blah") == True
        assert union.contains("other") == True

    def test_intersection(self):
        elements1 = ["1", "2", "5", "9"]
        elements2 = ["9", "2", "4", "3"]

        hs = HashSet(elements1)
        other_hs = HashSet(elements2)

        intersection = hs.intersection(other_hs)

        assert intersection.contains("9") == True
        assert intersection.contains("2") == True

        assert intersection.contains("1") == False
        assert intersection.contains("5") == False
        assert intersection.contains("4") == False
        assert intersection.contains("3") == False

    def test_difference(self):
        elements1 = ["1", "2", "5", "9"]
        elements2 = ["9", "2", "4", "3"]

        hs = HashSet(elements1)
        other_hs = HashSet(elements2)

        difference = hs.difference(other_hs)

        assert difference.contains("1") == True
        assert difference.contains("5") == True

        assert difference.contains("9") == False
        assert difference.contains("2") == False
        assert difference.contains("4") == False
        assert difference.contains("3") == False

    def test_is_subset(self):
        elements1 = ["1", "4", "6"]
        elements2 = ["1", "4"]

        hs = HashSet(elements1)
        other_hs = HashSet(elements2)

        assert other_hs.is_subset(hs) == True
        assert hs.is_subset(other_hs) == False
        other_hs.add("7")
        assert other_hs.is_subset(hs) == False


if __name__ == '__main__':
    unittest.main()
