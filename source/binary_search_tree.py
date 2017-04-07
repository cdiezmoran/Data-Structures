#!python

class BinaryNode(object):

    def __init__(self, data):
        """Initialize this node with the given data"""
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        """Return a string representation of this node"""
        return 'BinaryNode({})'.format(repr(self.data))

    def is_leaf(self):
        if self.left is None and self.right is None:
            return True
        return False

    def is_internal(self):
        return not self.is_leaf()

class BinarySearchTree(object):

    def __init__(self, iterable=None):
        self.root = None
        self.size = 0
        if iterable:
            self._insert_initial(iterable)

    def _insert_initial(self, iterable):
        mid_i = len(iterable) / 2
        left_i = mid_i - 1
        right_i = mid_i + 1
        self.insert(iterable[mid_i])

        for i in xrange(mid_i):
            left_i -= i
            right_i += i
            if left_i >= 0:
                self.insert(iterable[left_i])
            if right_i < len(iterable):
                self.insert(iterable[right_i])

    def insert(self, data, current=None):
        if self.root is None:
            new_node = BinaryNode(data)
            self.root = new_node
            self.size += 1
            return

        if current is None:
            current = self.root

        if data < current.data:
            if current.left is not None:
                return self.insert(data, current.left)
            new_node = BinaryNode(data)
            current.left = new_node
        else:
            if current.right is not None:
                return self.insert(data, current.right)
            new_node = BinaryNode(data)
            current.right = new_node

        self.size += 1
        return

    def search(self, data, current=None):
        pass

    def delete(self, data):
        pass
