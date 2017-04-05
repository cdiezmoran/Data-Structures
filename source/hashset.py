#!python

from hashtable import HashTable

class HashSet(object):
    def __init__(self, elements=None):
        if elements is not None:
            self.hash_table = HashTable(len(elements) * 2)
            for element in elements:
                self.hash_table.set(element, 0)
            self.size = self.hash_table.size
        else:
            self.hash_table = HashTable()

    def contains(self, element):
        return self.hash_table.contains(element)

    def add(self, element):
        if self.hash_table.contains(element):
            return

        self.hash_table.set(element, 0)
        self.size = self.hash_table.size

    def remove(self, element):
        if self.hash_table.contains(element):
            self.hash_table.delete(element)
            self.size = self.hash_table.size
        else:
            raise ValueError('Element not found: {}'.format(element))

    def union(self, other_set):
        new_set = HashSet()
        for key in self.hash_table.keys():
            new_set.add(key)
        for other_key in other_set.hash_table.keys():
            new_set.add(other_key)

        return new_set

    def intersection(self, other_set):
        new_set = HashSet()
        for key in self.hash_table.keys():
            for other_key in other_set.hash_table.keys():
                if key == other_key:
                    new_set.add(key)
                    break

        return new_set

    def difference(self, other_set):
        new_set = HashSet()
        for key in self.hash_table.keys():
            different = True
            for other_key in other_set.hash_table.keys():
                if key == other_key:
                    different = False
                    break
            if different:
                new_set.add(key)

        return new_set

    def is_subset(self, other_set):
        for key in self.hash_table.keys():
            if other_set.contains(key) is False:
                return False
        return True
