import unittest

from persistent_bst.node.node import Node

class NodeTest(unittest.TestCase):
  def test_constructor(self):
    node = Node(1)
    self.assertEqual(node.value, 1)
    self.assertEqual(node.left, None)
    self.assertEqual(node.right, None)

    self.assertRaises(ValueError, lambda: Node(None))