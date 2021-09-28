import unittest

from retroactive_heap.current_heap.current_heap import CurrentHeap
from retroactive_heap.current_heap.simple_current_heap import SimpleCurrentHeap
from retroactive_heap.heap import Heap
from retroactive_heap.interface import NewHeap
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
