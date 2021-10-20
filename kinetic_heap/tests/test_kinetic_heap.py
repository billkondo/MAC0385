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
                id_list=["0"],
            ),
        )
        self.assertRaises(
            ValueError,
            lambda: KineticHeap(
                n=1,
                id_list=["0"],
                x0_list=[0],
            ),
        )

        kinetic_heap = KineticHeap()
        self.assertEqual(kinetic_heap.t, 0)
        self.assertEqual(kinetic_heap.n, 0)
