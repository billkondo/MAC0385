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
    def setUp(self):
        self.heap: CurrentHeap = self.CurrentHeap()

    def test_current_heap(self):
        self.heap.insert(10, 20)
        self.heap.insert(15, 10)
        self.heap.insert(5, 30)
        self.heap.insert(7, 3)
        self.heap.insert(20, 2)

        self.assertEqual(self.heap.print(), "20 7 15 10 5")
        self.assertEqual(self.heap.min(20).key, 7)

        self.heap.delete(10)
        self.assertEqual(self.heap.print(), "20 7 15 5")
        self.assertEqual(self.heap.min(30).key, 5)

        self.heap.delete(5)
        self.assertEqual(self.heap.print(), "20 7 15")
        self.assertEqual(self.heap.min(2).key, 20)

    def test_insert_repeated_key(self):
        self.heap.insert(20, 10)
        self.assertRaises(ValueError, lambda: self.heap.insert(20, 30))
