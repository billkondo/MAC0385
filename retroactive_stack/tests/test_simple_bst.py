import unittest

from retroactive_stack.bst.simple_bst import SimpleBST
from retroactive_stack.operation import Operation


class SimpleBSTTest(unittest.TestCase):
    def test_insert(self):
        bst = SimpleBST()
        operations = [
            Operation(type=1, value="A"),
            Operation(type=1, value="B"),
            Operation(type=-1),
        ]

        bst.insert(1, operations[0])
        bst.insert(3, operations[2])
        bst.insert(2, operations[1])

        self.assertListEqual(bst.operations(), operations)

    def test_delete(self):
        bst = SimpleBST()
        operations = [Operation(type=1, value="A"), Operation(type=-1)]

        bst.insert(1, operations[0])
        bst.insert(2, operations[1])

        bst.delete(2)

        self.assertEqual(bst.operations(), [operations[0]])

    def test_kth(self):
        bst = SimpleBST()
        operations = [
            Operation(type=1, value="A"),
            Operation(type=1, value="B"),
            Operation(type=-1),
            Operation(type=1, value="C"),
        ]

        bst.insert(1, operations[0])
        bst.insert(3, operations[1])
        bst.insert(5, operations[2])
        bst.insert(7, operations[3])

        self.assertEqual(bst.kth(2, 1), "A")

        self.assertEqual(bst.kth(4, 1), "B")
        self.assertEqual(bst.kth(4, 2), "A")

        self.assertEqual(bst.kth(5, 1), "A")

        self.assertEqual(bst.kth(7, 2), "A")

        self.assertEqual(bst.kth(8, 1), "C")

    def test_count_less_than(self):
        bst = SimpleBST()
        operations = [
            Operation(type=1, value="A"),
            Operation(type=1, value="B"),
            Operation(type=-1),
            Operation(type=1, value="C"),
        ]

        bst.insert(1, operations[0])
        bst.insert(3, operations[1])
        bst.insert(5, operations[2])
        bst.insert(7, operations[3])

        self.assertEqual(bst.count_less_than(6), 3)
        self.assertEqual(bst.count_less_than(3), 2)
        self.assertEqual(bst.count_less_than(8), 4)
