import unittest

from persistent_bst.node.node import Node
from persistent_bst.bst import BST

class BSTTest(unittest.TestCase):
  def test_constructor(self):
    bst_empty = BST()
    self.assertEqual(bst_empty.root, None)

    root = Node(1)
    bst = BST(root)
    self.assertEqual(bst.root, root)

    self.assertRaises(TypeError, lambda: BST('invalid'))