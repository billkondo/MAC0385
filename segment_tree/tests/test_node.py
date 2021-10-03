import unittest

from segment_tree.node import Node


class TestNode(unittest.TestCase):
    def test_node(self):
        node = Node(10, 15)

        self.assertEqual(node.left, 10)
        self.assertEqual(node.right, 15)
