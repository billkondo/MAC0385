import unittest

from persistent_deque.node import Node

class NodeTest(unittest.TestCase):
  def test_constructor(self):
    parent = Node(5, None, 0)
    node = Node(2, parent, 2)

    self.assertEqual(parent.value, 5)
    self.assertEqual(parent.parent, None)
    self.assertEqual(parent.depth, 0)

    self.assertEqual(node.value, 2)
    self.assertEqual(node.parent, parent)
    self.assertEqual(node.depth, 2)

  def test_constructor_raises(self):
    self.assertRaises(TypeError, lambda: Node("invalid", None, 0))
    self.assertRaises(TypeError, lambda: Node(5, 4, 0))
    self.assertRaises(TypeError, lambda: Node(2, None, "invalid"))
    self.assertRaises(ValueError, lambda: Node(2, None, -5))