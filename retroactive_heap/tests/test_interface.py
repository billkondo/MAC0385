import unittest

from retroactive_heap.current_heap.current_heap import CurrentHeap
from retroactive_heap.current_heap.simple_current_heap import SimpleCurrentHeap
from retroactive_heap.heap import Heap
from retroactive_heap.interface import AddDeleteMin, AddInsert, NewHeap
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
        self.assertEqual(heap.current_heap.print(), "5 8")
        AddDeleteMin(heap, 6)
        self.assertEqual(heap.current_heap.print(), "8")
        AddInsert(heap, 7, 4)
        AddInsert(heap, 8, 6)
        self.assertEqual(heap.current_heap.print(), "4 6 8")
        AddDeleteMin(heap, 9)
        self.assertEqual(heap.current_heap.print(), "6 8")
        AddInsert(heap, 10, 7)
        AddInsert(heap, 11, 3)
        AddDeleteMin(heap, 12)
        AddDeleteMin(heap, 13)
        AddInsert(heap, 15, 2)
        AddDeleteMin(heap, 16)
        AddInsert(heap, 17, 9)

        self.assertEqual(heap.current_heap.print(), "7 8 9")

        AddDeleteMin(heap, 5)
        self.assertEqual(heap.current_heap.print(), "7 9")

        AddInsert(heap, 14, 0)
        self.assertEqual(heap.current_heap.print(), "2 7 9")

        AddDeleteMin(heap, 11)
        self.assertEqual(heap.current_heap.print(), "2 9")

    def test_add_delete_min_error(self):
        heap = Heap()

        AddInsert(heap, 2, 1)
        self.assertRaises(RuntimeError, lambda: AddDeleteMin(heap, 1))
        AddDeleteMin(heap, 3)
        AddInsert(heap, 0, 10)
        AddDeleteMin(heap, 1)
        self.assertRaises(RuntimeError, lambda: AddDeleteMin(heap, 5))
