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
            for item in iterable:
                self.insert(item)


    """def _insert_initial(self, iterable):
        iterable.sort()
        mid_i = len(iterable) / 2

        self.insert(iterable[mid_i])

        count = 1
        offset_left = mid_i
        offset_right = 0

        while count < len(iterable):"""

    def _find_node(self, item):
        """Return the node containing the given item in this binary search tree,
        or None if the given item is not found"""
        # Start with the root node
        node = self.root
        # Loop until we descend past the closest leaf node
        while node is not None:
            # Check if the given item matches the node's data
            if item == node.data:
                # Return the found node
                return node
            # Check if the given item is less than the node's data
            elif item < node.data:
                # Descend to the node's left child
                node = node.left
            # Check if the given item is greater than the node's data
            elif item > node.data:
                # Descend to the node's right child
                node = node.right
        # Not found
        return None

    def _find_parent_node(self, item):
        """Return the parent node of where the given item is (or would be) in
        this binary search tree, or None if this tree has only a root node"""
        # Start with the root node and keep track of its parent
        node = self.root
        parent = None
        # Loop until we descend past the closest leaf node
        while node is not None:
            # Check if the given item matches the node's data
            if item == node.data:
                # Return the parent of the found node
                return parent
            # Check if the given item is less than the node's data
            elif item < node.data:
                # Update the parent and descend to the node's left child
                parent = node
                node = node.left
            # Check if the given item is greater than the node's data
            elif item > node.data:
                # Update the parent and descend to the node's right child
                parent = node
                node = node.right
        # Not found
        return parent

    def is_empty(self):
        if self.root is None:
            return True
        return False

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
        if self.is_empty():
            return None

        if current is None:
            current = self.root

        if data == current.data:
            return data

        if current.is_leaf():
            return None

        if data < current.data:
            return self.search(data, current.left)
        elif data >= current.data:
            return self.search(data, current.right)


    def delete(self, data):
        node = self._find_node(data)

        if node is None:
            raise ValueError('Data given is not in the tree')

        parent = self._find_parent_node(data)

        is_left_node = False
        if parent.left.data == data:
            is_left_node = True

        if node.is_leaf():
            if parent.left.data == data:
                parent.left = None
            elif parent.right.data == data:
                parent.right = None
        else :
            replace_node = node.right
            cutoff_node = node.left
            if replace_node is None:
                replace_node = node.left
                cutoff_node = node.right

            if self.root == node:
                self.root = replace_node
            else :
                if is_left_node:
                    parent.left = replace_node
                else :
                    parent.right = replace_node

            if cutoff_node is not None:
                new_parent = self._find_parent_node(cutoff_node)
                if new_parent.left is None:
                    new_parent.left = cutoff_node
                else:
                    new_parent.right = cutoff_node

        self.size -= 1
