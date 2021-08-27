import unittest

from persistent_deque.node import Node
from persistent_deque.node.interface import Depth, AddLeaf

class NodeInterfaceTest(unittest.TestCase):
  def test_depth(self):
    self.assertEqual(Depth(Node(4, None, 10)), 10)

    self.assertRaises(ValueError, lambda: Depth(None))
    self.assertRaises(TypeError, lambda: Depth('invalid'))

  def test_add_leaf(self):
    root = Node(0, None, 0)
    node = AddLeaf(1, root)

    self.assertEqual(node.value, 1)
    self.assertEqual(node.parent, root)
    self.assertEqual(node.depth, 1)