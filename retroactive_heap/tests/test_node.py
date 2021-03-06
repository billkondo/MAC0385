import unittest

from retroactive_heap.current_heap.node import Node


class TestNode(unittest.TestCase):
    def test_node(self):
        self.assertRaises(TypeError, lambda: Node(key="123"))
        self.assertRaises(TypeError, lambda: Node(time="123"))

        node = Node(key=10, time=20)
        self.assertEqual(node.key, 10)
        self.assertEqual(node.time, 20)
