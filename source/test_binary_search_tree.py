#!python

from binary_search_tree import BinarySearchTree, BinaryNode
import unittest


class NodeTest(unittest.TestCase):

    def test_init(self):
        data = 'ABC'
        node = BinaryNode(data)
        assert node.data is data
        assert node.left is None
        assert node.right is None
        assert node.is_leaf() == True
        assert node.is_internal() == False


class LinkedListTest(unittest.TestCase):

    def test_init(self):
        bst = BinarySearchTree()
        assert bst.root is None
        assert bst.size == 0

    def test_insert(self):
        bst = BinarySearchTree()
        bst.insert("Nick")
        assert bst.root.data == "Nick"
        bst.insert("Alex")
        assert bst.root.left.data == "Alex"
        bst.insert("Tassos")
        assert bst.root.right.data == "Tassos"
        bst.insert("Carlos")
        left_node = bst.root.left
        assert left_node.right.data == "Carlos"


if __name__ == '__main__':
    unittest.main()
