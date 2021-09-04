import unittest

from persistent_bst.bst import BST
from persistent_bst.interface import NewBST, CopyBST, Insert
from persistent_bst.node.node import Node

class InterfaceTest(unittest.TestCase):
  def test_new_bst(self):
    bst = NewBST()
    self.assertEqual(bst.root, None)

  def test_copy_bst(self):
    self.assertRaises(ValueError, lambda: CopyBST(None))

    bst = BST(Node(5))
    bst_copy = CopyBST(bst)

    self.assertEqual(bst.root.value, bst_copy.root.value)
    self.assertNotEqual(bst.root, bst_copy.root)

  def test_insert(self):
    self.assertRaises(TypeError, lambda: Insert('invalid', 5))
    self.assertRaises(ValueError, lambda: Insert(None, 5))

    bst_0 = NewBST()
    
    bst_1 = Insert(bst_0, 5)
    self.assertEqual(bst_1.root.value, 5)
    self.assertNotEqual(bst_0.root, bst_1.root)

    bst_2 = Insert(bst_1, 10)
    self.assertEqual(bst_2.root.right.value, 10)
    self.assertNotEqual(bst_1.root, bst_2.root)

    bst_3 = Insert(bst_2, 5)
    self.assertEqual(bst_3.root.left.value, 5)
    self.assertNotEqual(bst_2.root, bst_3.root)
