import unittest

from kinetic_heap import KineticHeap


class TestKineticHeap(unittest.TestCase):
    def test_constructor(self):
        self.assertRaises(TypeError, lambda: KineticHeap(n="invalid"))
        self.assertRaises(ValueError, lambda: KineticHeap(n=5))
        self.assertRaises(
            ValueError,
            lambda: KineticHeap(
                n=1,
                id_list=[0],
            ),
        )
        self.assertRaises(
            ValueError,
            lambda: KineticHeap(
                n=1,
                id_list=[0],
                x0_list=[0],
            ),
        )

        kinetic_heap = KineticHeap(
            id_list=[0],
            x0_list=[5],
            speed_list=[10],
            n=1,
        )

        self.assertEqual(kinetic_heap.max(), 0)

    def test_kinetic_heap_01(self):
        kinetic_heap = KineticHeap([10, 20], [5, 0], [-1, 1], 2)

        self.assertEqual(kinetic_heap.max(), 10)
        kinetic_heap.advance(1)
        self.assertEqual(kinetic_heap.max(), 10)
        kinetic_heap.advance(2.5)
        self.assertEqual(kinetic_heap.max(), 10)
        kinetic_heap.advance(3.0)
        self.assertEqual(kinetic_heap.max(), 20)
        kinetic_heap.advance(5.0)
        self.assertEqual(kinetic_heap.max(), 20)
        kinetic_heap.change(10, 1)
        kinetic_heap.change(20, -1)
        self.assertEqual(kinetic_heap.max(), 20)
        kinetic_heap.advance(7.5)
        self.assertEqual(kinetic_heap.max(), 20)
        kinetic_heap.advance(8)
        self.assertEqual(kinetic_heap.max(), 10)

    def test_kinetic_heap_02(self):
        kinetic_heap = KineticHeap(
            [1, 2, 3, 4],
            [3, 10, 20, 15],
            [5, -2, 4, -3],
            4,
        )

        self.assertEqual(kinetic_heap.max(), 3)
        kinetic_heap.advance(2)
        self.assertEqual(kinetic_heap.max(), 3)
        kinetic_heap.delete_max()
        self.assertEqual(kinetic_heap.max(), 1)
        kinetic_heap.delete(1)
        self.assertEqual(kinetic_heap.max(), 4)
        kinetic_heap.insert(5, 10, 4)
        self.assertEqual(kinetic_heap.max(), 5)
        kinetic_heap.insert(6, 12, -3)
        self.assertEqual(kinetic_heap.max(), 6)
        kinetic_heap.advance(5)
        self.assertEqual(kinetic_heap.max(), 5)
        kinetic_heap.delete(5)
        self.assertEqual(kinetic_heap.max(), 6)
        kinetic_heap.advance(7)
        self.assertEqual(kinetic_heap.max(), 6)
