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

    def test_size(self):
        bst = SimpleBST()
        operations = [
            Operation(type=1, value="A"),
            Operation(type=1, value="B"),
            Operation(type=1, value="C"),
            Operation(type=-1),
            Operation(type=-1),
        ]

        for idx, op in enumerate(operations):
            bst.insert(idx + 1, op)

        self.assertEqual(bst.size(1), 1)
        self.assertEqual(bst.size(2), 2)
        self.assertEqual(bst.size(3), 3)
        self.assertEqual(bst.size(4), 2)
        self.assertEqual(bst.size(5), 1)
        self.assertEqual(bst.size(6), 1)

    def test_print(self):
        bst = SimpleBST()
        operations = [
            Operation(type=1, value="A"),
            Operation(type=-1),
            Operation(type=1, value="B"),
            Operation(type=1, value="C"),
            Operation(type=-1),
        ]

        for idx, op in enumerate(operations):
            bst.insert(idx + 1, op)

        self.assertEqual(bst.print(1), "A")
        self.assertEqual(bst.print(2), "")
        self.assertEqual(bst.print(3), "B")
        self.assertEqual(bst.print(4), "C B")
        self.assertEqual(bst.print(5), "B")
        self.assertEqual(bst.print(6), "B")
