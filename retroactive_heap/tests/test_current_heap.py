import unittest

from parameterized import parameterized_class
from retroactive_heap.current_heap.avl_current_heap import AVLCurrentHeap
from retroactive_heap.current_heap.current_heap import CurrentHeap
from retroactive_heap.current_heap.simple_current_heap import SimpleCurrentHeap


@parameterized_class(
    [
        {"CurrentHeap": SimpleCurrentHeap},
        {"CurrentHeap": AVLCurrentHeap},
    ]
)
class TestCurrentHeap(unittest.TestCase):
    def test_current_heap(self):
        heap: CurrentHeap = self.CurrentHeap()

        heap.insert(10, 20)
        heap.insert(15, 10)
        heap.insert(5, 30)
        heap.insert(7, 3)
        heap.insert(20, 2)

        self.assertEqual(heap.print(), "20 7 15 10 5")
        self.assertEqual(heap.min(20).key, 7)

        heap.delete(10)
        self.assertEqual(heap.print(), "20 7 15 5")
        self.assertEqual(heap.min(30).key, 5)

        heap.delete(5)
        self.assertEqual(heap.print(), "20 7 15")
        self.assertEqual(heap.min(2).key, 20)
