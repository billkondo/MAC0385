import unittest

from parameterized import parameterized_class
from retroactive_heap.current_heap.avl_current_heap import AVLCurrentHeap
from retroactive_heap.current_heap.current_heap import CurrentHeap
from retroactive_heap.current_heap.simple_current_heap import SimpleCurrentHeap
from retroactive_heap.interface import (
    AddDeleteMin,
    AddInsert,
    Delete,
    Min,
    NewHeap,
    Print,
)
from retroactive_heap.operations_bst.avl_bst import AVLBST
from retroactive_heap.operations_bst.bst import BST
from retroactive_heap.operations_bst.simple_bst import SimpleBST


@parameterized_class(
    [
        {"CurrentHeap": SimpleCurrentHeap, "BST": SimpleBST},
        {"CurrentHeap": AVLCurrentHeap, "BST": AVLBST},
    ]
)
class TestInterface(unittest.TestCase):
    def setUp(self):
        self.heap = NewHeap(
            current_heap=self.CurrentHeap(),
            operations_bst=self.BST(),
        )

    def test_new_heap(self):
        current_heap: CurrentHeap = self.CurrentHeap()
        bst: BST = self.BST()
        configured_heap = NewHeap(
            current_heap=current_heap,
            operations_bst=bst,
        )
        self.assertEqual(configured_heap.current_heap, current_heap)
        self.assertEqual(configured_heap.operations_bst, bst)

        default_heap = NewHeap()
        self.assertIsInstance(default_heap.current_heap, CurrentHeap)
        self.assertIsInstance(default_heap.operations_bst, BST)

    def test_add(self):
        AddInsert(self.heap, 1, 1)
        AddInsert(self.heap, 2, 5)
        AddDeleteMin(self.heap, 3)
        AddInsert(self.heap, 4, 8)
        self.assertEqual(Print(self.heap), "5 8")
        AddDeleteMin(self.heap, 6)
        self.assertEqual(Print(self.heap), "8")
        AddInsert(self.heap, 7, 4)
        AddInsert(self.heap, 8, 6)
        self.assertEqual(Print(self.heap), "4 6 8")
        AddDeleteMin(self.heap, 9)
        self.assertEqual(Print(self.heap), "6 8")
        AddInsert(self.heap, 10, 7)
        AddInsert(self.heap, 11, 3)
        AddDeleteMin(self.heap, 12)
        AddDeleteMin(self.heap, 13)
        AddInsert(self.heap, 15, 2)
        AddDeleteMin(self.heap, 16)
        AddInsert(self.heap, 17, 9)

        self.assertEqual(Print(self.heap), "7 8 9")

        AddDeleteMin(self.heap, 5)
        self.assertEqual(Print(self.heap), "7 9")

        AddInsert(self.heap, 14, 0)
        self.assertEqual(Print(self.heap), "2 7 9")

        AddDeleteMin(self.heap, 11)
        self.assertEqual(Print(self.heap), "2 9")

    def test_add_delete_min_error(self):
        AddInsert(self.heap, 2, 1)
        self.assertRaises(RuntimeError, lambda: AddDeleteMin(self.heap, 1))
        AddDeleteMin(self.heap, 3)
        AddInsert(self.heap, 0, 10)
        AddDeleteMin(self.heap, 1)
        self.assertRaises(RuntimeError, lambda: AddDeleteMin(self.heap, 5))

    def test_delete_01(self):
        self.assertRaises(RuntimeError, lambda: Delete(self.heap, 0))

        AddInsert(self.heap, 1, 1)
        AddInsert(self.heap, 2, 2)
        AddInsert(self.heap, 3, 3)
        AddDeleteMin(self.heap, 4)
        self.assertEqual(Print(self.heap), "2 3")

        Delete(self.heap, 1)
        self.assertEqual(Print(self.heap), "3")

        Delete(self.heap, 4)
        self.assertEqual(Print(self.heap), "2 3")

        Delete(self.heap, 3)
        self.assertEqual(Print(self.heap), "2")

        AddDeleteMin(self.heap, 4)
        self.assertEqual(Print(self.heap), "")

        self.assertRaises(RuntimeError, lambda: Delete(self.heap, 2))

    def test_delete_02(self):
        AddInsert(self.heap, 1, 3)
        AddInsert(self.heap, 2, 1)
        AddInsert(self.heap, 3, 2)
        AddDeleteMin(self.heap, 4)
        AddDeleteMin(self.heap, 5)
        AddInsert(self.heap, 6, 0)

        self.assertEqual(Print(self.heap), "0 3")
        self.assertEqual(Min(self.heap), 0)

        Delete(self.heap, 2)
        self.assertEqual(Print(self.heap), "0")
        self.assertEqual(Min(self.heap), 0)

    def test_min(self):
        self.assertEqual(Min(self.heap), None)

        AddInsert(self.heap, 1, 5)
        AddInsert(self.heap, 5, 3)
        AddInsert(self.heap, 10, 10)
        AddInsert(self.heap, 15, 8)

        self.assertEqual(Print(self.heap), "3 5 8 10")
        self.assertEqual(Min(self.heap), 3)

        AddDeleteMin(self.heap, 3)
        self.assertEqual(Print(self.heap), "3 8 10")
        self.assertEqual(Min(self.heap), 3)

        AddDeleteMin(self.heap, 8)
        self.assertEqual(Print(self.heap), "8 10")
        self.assertEqual(Min(self.heap), 8)

        Delete(self.heap, 8)
        self.assertEqual(Print(self.heap), "3 8 10")
        self.assertEqual(Min(self.heap), 3)
