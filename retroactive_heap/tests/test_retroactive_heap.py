import unittest
from time import process_time

from retroactive_heap.current_heap.avl_current_heap import AVLCurrentHeap
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
from retroactive_heap.operations_bst.simple_bst import SimpleBST


def with_assert(f):
    def wrapper(*args):
        self = args[0]

        f(*args)

        self.assertEqual(Print(self.simple_heap), Print(self.avl_heap))
        self.assertEqual(Min(self.simple_heap), Min(self.avl_heap))

    return wrapper


class TestRetroactiveHeap(unittest.TestCase):
    def setUp(self):
        self.simple_heap = NewHeap(SimpleCurrentHeap(), SimpleBST())
        self.avl_heap = NewHeap(AVLCurrentHeap(), AVLBST())

    @with_assert
    def insert(self, time: int, key: int):
        AddInsert(self.simple_heap, time, key)
        AddInsert(self.avl_heap, time, key)

    @with_assert
    def delete_min(self, time: int):
        AddDeleteMin(self.simple_heap, time)
        AddDeleteMin(self.avl_heap, time)

    @with_assert
    def delete(self, time: int):
        Delete(self.simple_heap, time)
        Delete(self.avl_heap, time)

    def test_retroactive_heap_01(self):
        self.insert(5, 100)
        self.insert(10, 50)
        self.insert(15, 80)
        self.delete_min(20)
        self.delete_min(25)
        self.insert(30, 90)
        self.insert(35, 70)
        self.insert(40, 60)
        self.insert(45, 65)
        self.delete_min(50)
        self.delete_min(55)
        self.delete_min(60)

        self.delete(15)
        self.assertEqual(Min(self.avl_heap), 90)

        self.insert(7, 30)
        self.delete(7)
        self.insert(8, 30)

        self.delete_min(32)
        self.delete(20)
        self.delete(40)
        self.insert(46, 15)

    def test_retroactive_heap_02(self):
        for i in range(1, 50):
            self.insert(i, 2 * i)

        for i in range(50, 75):
            self.delete_min(i)

        for i in range(75, 125):
            self.insert(i, 2 * i)

        for i in range(125, 150):
            self.delete_min(i)

        for i in range(40, 104):
            self.delete(i)

    def test_retroactive_heap_03(self):
        for i in range(1, 500):
            if i % 10 == 0:
                self.delete_min(i)
            else:
                self.insert(i, i ** 2)

        for i in range(50, 100):
            self.delete(i)

        for i in range(200, 250):
            self.delete(i)

        for i in range(50, 100):
            self.insert(i, -i)

    def test_retroactive_heap_stress(self):
        start_time = process_time()
        time_limit = 7.5

        for i in range(0, 5000):
            AddInsert(self.avl_heap, i, 5 * i)

            if process_time() - start_time > time_limit:
                raise TimeoutError("Time limit exceeded")

        for i in range(10000, 15000):
            AddDeleteMin(self.avl_heap, i)

            if process_time() - start_time > time_limit:
                raise TimeoutError("Time limit exceeded")

        for i in range(5000, 10000):
            key = 3 * i
            if key % 5 == 0:
                key = key + 1
            AddInsert(self.avl_heap, i, key)

            if process_time() - start_time > time_limit:
                raise TimeoutError("Time limit exceeded")

        for i in range(12500, 14000):
            Delete(self.avl_heap, i)

            if process_time() - start_time > time_limit:
                raise TimeoutError("Time limit exceeded")

        for i in range(2500, 7500):
            Delete(self.avl_heap, i)

            if process_time() - start_time > time_limit:
                raise TimeoutError("Time limit exceeded")

        duration = process_time() - start_time

        self.assertLessEqual(duration, time_limit)
