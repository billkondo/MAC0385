import math
import unittest

from retroactive_heap.operations_bst.simple_bst import SimpleBST


class TestSimpleBST(unittest.TestCase):
    def test_simple_bst_01(self):
        bst = SimpleBST()

        bst.insert(time=1, key=4, type=+1)
        bst.insert(time=2, key=3, type=+1)
        bst.insert(time=3, key=7, type=0)
        bst.insert(time=4, type=-1)
        bst.insert(time=5, type=-1)
        bst.insert(time=6, key=1, type=+1)
        bst.insert(time=7, type=-1)
        bst.insert(time=8, key=6, type=0)
        bst.insert(time=9, key=2, type=+1)
        bst.insert(time=10, key=5, type=+1)
        bst.insert(time=11, type=-1)
        bst.insert(time=12, type=-1)

        self.assertEqual(bst.previous_bridge_time(1), -math.inf)
        self.assertEqual(bst.previous_bridge_time(2), -math.inf)
        self.assertEqual(bst.previous_bridge_time(3), -math.inf)
        self.assertEqual(bst.previous_bridge_time(4), -math.inf)
        self.assertEqual(bst.previous_bridge_time(5), 5)
        self.assertEqual(bst.previous_bridge_time(6), 5)
        self.assertEqual(bst.previous_bridge_time(7), 7)
        self.assertEqual(bst.previous_bridge_time(8), 8)
        self.assertEqual(bst.previous_bridge_time(9), 8)
        self.assertEqual(bst.previous_bridge_time(10), 8)
        self.assertEqual(bst.previous_bridge_time(11), 8)
        self.assertEqual(bst.previous_bridge_time(12), 12)

        self.assertEqual(bst.next_bridge_time(1), 5)
        self.assertEqual(bst.next_bridge_time(2), 5)
        self.assertEqual(bst.next_bridge_time(3), 5)
        self.assertEqual(bst.next_bridge_time(4), 5)
        self.assertEqual(bst.next_bridge_time(5), 5)
        self.assertEqual(bst.next_bridge_time(6), 7)
        self.assertEqual(bst.next_bridge_time(7), 7)
        self.assertEqual(bst.next_bridge_time(8), 8)
        self.assertEqual(bst.next_bridge_time(9), 12)
        self.assertEqual(bst.next_bridge_time(10), 12)
        self.assertEqual(bst.next_bridge_time(11), 12)
        self.assertEqual(bst.next_bridge_time(12), 12)

        self.assertEqual(bst.max(1).key, 5)

        bst.delete(2)
        bst.delete(4)
        bst.delete(5)
        bst.delete(6)

        self.assertEqual(bst.next_bridge_time(1), 7)
        self.assertEqual(bst.next_bridge_time(3), 7)

    def test_simple_bst_02(self):
        bst = SimpleBST()

        bst.insert(time=1, key=3, type=+1)
        bst.insert(time=2, type=-1)
        bst.insert(time=3, key=1, type=+1)
        bst.insert(time=4, key=2, type=+1)
        bst.insert(time=5, type=-1)
        bst.insert(time=6, type=-1)
        bst.insert(time=7, key=4, type=+1)

        self.assertEqual(bst.previous_bridge_time(1), -math.inf)
        self.assertEqual(bst.next_bridge_time(1), 2)

        self.assertEqual(bst.previous_bridge_time(4), 2)
        self.assertEqual(bst.next_bridge_time(4), 6)

        self.assertEqual(bst.previous_bridge_time(7), 6)
        self.assertEqual(bst.next_bridge_time(7), math.inf)

        self.assertEqual(bst.max(5).key, 4)

        bst.delete(7)

        self.assertEqual(bst.max(1).key, 3)
        self.assertEqual(bst.max(2).key, 2)
        self.assertEqual(bst.max(6), None)
