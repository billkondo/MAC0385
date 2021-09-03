import unittest

from persistent_bst.interface import NewBST

class InterfaceTest(unittest.TestCase):
  def test_new_bst(self):
    bst = NewBST()
    self.assertEqual(bst.root, None)
