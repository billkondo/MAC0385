import unittest

from retroactive_heap.current_heap.current_heap import CurrentHeap
from retroactive_heap.current_heap.simple_current_heap import SimpleCurrentHeap
from retroactive_heap.heap import Heap
from retroactive_heap.interface import (
    AddDeleteMin,
    AddInsert,
    Delete,
    Min,
    NewHeap,
    Print,
)
from retroactive_heap.operations_bst.bst import BST
from retroactive_heap.operations_bst.simple_bst import SimpleBST


class TestInterface(unittest.TestCase):
    def test_new_heap(self):
        current_heap = SimpleCurrentHeap()
        bst = SimpleBST()
        configured_heap = Heap(
            current_heap=current_heap,
            operations_bst=bst,
        )
        self.assertEqual(configured_heap.current_heap, current_heap)
        self.assertEqual(configured_heap.operations_bst, bst)

        heap = NewHeap()
        self.assertIsInstance(heap.current_heap, CurrentHeap)
        self.assertIsInstance(heap.operations_bst, BST)

    def test_add(self):
        heap = Heap()

        AddInsert(heap, 1, 1)
        AddInsert(heap, 2, 5)
        AddDeleteMin(heap, 3)
        AddInsert(heap, 4, 8)
        self.assertEqual(Print(heap), "5 8")
        AddDeleteMin(heap, 6)
        self.assertEqual(Print(heap), "8")
        AddInsert(heap, 7, 4)
        AddInsert(heap, 8, 6)
        self.assertEqual(Print(heap), "4 6 8")
        AddDeleteMin(heap, 9)
        self.assertEqual(Print(heap), "6 8")
        AddInsert(heap, 10, 7)
        AddInsert(heap, 11, 3)
        AddDeleteMin(heap, 12)
        AddDeleteMin(heap, 13)
        AddInsert(heap, 15, 2)
        AddDeleteMin(heap, 16)
        AddInsert(heap, 17, 9)

        self.assertEqual(Print(heap), "7 8 9")

        AddDeleteMin(heap, 5)
        self.assertEqual(Print(heap), "7 9")

        AddInsert(heap, 14, 0)
        self.assertEqual(Print(heap), "2 7 9")

        AddDeleteMin(heap, 11)
        self.assertEqual(Print(heap), "2 9")

    def test_add_delete_min_error(self):
        heap = Heap()

        AddInsert(heap, 2, 1)
        self.assertRaises(RuntimeError, lambda: AddDeleteMin(heap, 1))
        AddDeleteMin(heap, 3)
        AddInsert(heap, 0, 10)
        AddDeleteMin(heap, 1)
        self.assertRaises(RuntimeError, lambda: AddDeleteMin(heap, 5))

    def test_delete_01(self):
        heap = Heap()

        self.assertRaises(RuntimeError, lambda: Delete(heap, 0))

        AddInsert(heap, 1, 1)
        AddInsert(heap, 2, 2)
        AddInsert(heap, 3, 3)
        AddDeleteMin(heap, 4)
        self.assertEqual(Print(heap), "2 3")

        Delete(heap, 1)
        self.assertEqual(Print(heap), "3")

        Delete(heap, 4)
        self.assertEqual(Print(heap), "2 3")

        Delete(heap, 3)
        self.assertEqual(Print(heap), "2")

        AddDeleteMin(heap, 4)
        self.assertEqual(Print(heap), "")

        self.assertRaises(RuntimeError, lambda: Delete(heap, 2))

    def test_delete_02(self):
        heap = Heap()

        AddInsert(heap, 1, 3)
        AddInsert(heap, 2, 1)
        AddInsert(heap, 3, 2)
        AddDeleteMin(heap, 4)
        AddDeleteMin(heap, 5)
        AddInsert(heap, 6, 0)

        self.assertEqual(Print(heap), "0 3")
        self.assertEqual(Min(heap), 0)

        Delete(heap, 2)
        self.assertEqual(Print(heap), "0")
        self.assertEqual(Min(heap), 0)

    def test_min(self):
        heap = Heap()

        AddInsert(heap, 1, 5)
        AddInsert(heap, 5, 3)
        AddInsert(heap, 10, 10)
        AddInsert(heap, 15, 8)

        self.assertEqual(Print(heap), "3 5 8 10")
        self.assertEqual(Min(heap), 3)

        AddDeleteMin(heap, 3)
        self.assertEqual(Print(heap), "3 8 10")
        self.assertEqual(Min(heap), 3)

        AddDeleteMin(heap, 8)
        self.assertEqual(Print(heap), "8 10")
        self.assertEqual(Min(heap), 8)

        Delete(heap, 8)
        self.assertEqual(Print(heap), "3 8 10")
        self.assertEqual(Min(heap), 3)
