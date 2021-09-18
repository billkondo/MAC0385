import unittest

from persistent_bst.bst import BST
from persistent_bst.interface import (
    CopyBST,
    Delete,
    Empty,
    Insert,
    Min,
    NewBST,
    Print,
    Search,
)
from persistent_bst.node.node import Node


class InterfaceTest(unittest.TestCase):
    def setUp(self):
        self.bst = Insert(Insert(Insert(Insert(NewBST(), 2), 1), 4), 3)

    def test_empty(self):
        self.assertRaises(TypeError, lambda: Empty("invalid"))
        self.assertRaises(ValueError, lambda: Empty(None))

        self.assertTrue(Empty(NewBST()))
        self.assertFalse(Empty(Insert(NewBST(), 5)))

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
        self.assertRaises(TypeError, lambda: Insert("invalid", 5))
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

    def test_search(self):
        self.assertRaises(TypeError, lambda: Search("invalid", 5))
        self.assertRaises(ValueError, lambda: Search(None, 5))

        self.assertTrue(Search(self.bst, 1))
        self.assertTrue(Search(self.bst, 2))
        self.assertTrue(Search(self.bst, 3))
        self.assertTrue(Search(self.bst, 4))

        self.assertFalse(Search(self.bst, 0))
        self.assertFalse(Search(self.bst, 5))

    def test_delete(self):
        self.assertRaises(TypeError, lambda: Delete("invalid", 5))
        self.assertRaises(ValueError, lambda: Delete(None, 5))
        self.assertRaises(RuntimeError, lambda: Delete(self.bst, 5))

        bst = Delete(self.bst, 2)

        self.assertEqual(bst.root.value, 3)
        self.assertFalse(Search(bst, 2))

    def test_min(self):
        self.assertRaises(ValueError, lambda: Min(None))
        self.assertRaises(TypeError, lambda: Min("invalid"))
        self.assertRaises(ValueError, lambda: Min(NewBST()))

        self.assertEqual(Min(self.bst), 1)

    def test_print(self):
        self.assertEqual(Print(self.bst), "2 1 4 3")
