import unittest

from retroactive_heap.current_heap.current_heap import Node


class TestCurrentHeap(unittest.TestCase):
    def test_node(self):
        self.assertRaises(ValueError, lambda: Node(key="123"))
        self.assertRaises(ValueError, lambda: Node(time="123"))

        node = Node(key=10, time=20)
        self.assertEqual(node.key, 10)
        self.assertEqual(node.time, 20)
