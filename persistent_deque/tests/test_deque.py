import unittest

from persistent_deque.deque import Deque
from persistent_deque.node.node import Node


class DequeTest(unittest.TestCase):
    def setUp(self):
        self.node1 = Node(1, None, 0)
        self.node2 = Node(2, None, 1)

    def test_constructor(self):
        deque1 = Deque(self.node1, self.node2)
        deque2 = Deque(None, None)
        deque3 = Deque(self.node2, self.node1)

        self.assertEqual(deque1.first, self.node1)
        self.assertEqual(deque1.last, self.node2)

        self.assertEqual(deque2.first, None)
        self.assertEqual(deque2.last, None)

        self.assertEqual(deque3.first, self.node2)
        self.assertEqual(deque3.last, self.node1)

    def test_constructor_raises(self):
        self.assertRaises(TypeError, lambda: Deque("invalid"))
        self.assertRaises(TypeError, lambda: Deque(None, 4))
        self.assertRaises(TypeError, lambda: Deque(self.node1, "invalid"))
        self.assertRaises(ValueError, lambda: Deque(None, self.node1))
        self.assertRaises(ValueError, lambda: Deque(self.node1, None))
