import unittest

from retroactive_heap.current_heap.current_heap import CurrentHeap
from retroactive_heap.current_heap.simple_current_heap import SimpleCurrentHeap
from retroactive_heap.heap import Heap
from retroactive_heap.operations_bst.bst import BST
from retroactive_heap.operations_bst.simple_bst import SimpleBST


class TestHeap(unittest.TestCase):
    def test_heap(self):
        self.assertRaises(TypeError, lambda: Heap(current_heap="invalid"))
        self.assertRaises(TypeError, lambda: Heap(operations_bst="invalid"))

        current_heap = SimpleCurrentHeap()
        operations_bst = SimpleBST()
        heap = Heap(
            current_heap=current_heap,
            operations_bst=operations_bst,
        )

        self.assertEqual(heap.current_heap, current_heap)
        self.assertEqual(heap.operations_bst, operations_bst)

        self.assertIsInstance(heap.current_heap, CurrentHeap)
        self.assertIsInstance(heap.operations_bst, BST)
