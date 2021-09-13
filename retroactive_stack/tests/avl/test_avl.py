import unittest
from typing import List

from retroactive_stack.bst.avl.avl import AVL
from retroactive_stack.bst.avl.node import Sum
from retroactive_stack.operation import Operation


class AVLTest(unittest.TestCase):
    def setUp(self):
        self.operations: List[Operation] = [
            Operation(type=1, value="A"),
            Operation(type=1, value="B"),
            Operation(type=-1),
            Operation(type=1, value="C"),
            Operation(type=1, value="D"),
            Operation(type=-1),
        ]

        self.avl = AVL()

        self.avl.insert(key=5, operation=self.operations[0])
        self.avl.insert(key=10, operation=self.operations[1])
        self.avl.insert(key=15, operation=self.operations[2])
        self.avl.insert(key=20, operation=self.operations[3])
        self.avl.insert(key=25, operation=self.operations[4])
        self.avl.insert(key=30, operation=self.operations[5])

    def test_constructor(self):
        avl = AVL()
        self.assertIsNone(avl.root)

    def test_insert(self):
        self.assertEqual(Sum(self.avl.root), 2)

    def test_size(self):
        self.assertEqual(self.avl.size(20), 2)
        self.assertEqual(self.avl.size(25), 3)
        self.assertEqual(self.avl.size(30), 2)

    def test_kth(self):
        self.assertEqual(self.avl.kth(20, 2), "A")
        self.assertEqual(self.avl.kth(25, 2), "C")
        self.assertEqual(self.avl.kth(30, 2), "A")

    def test_print(self):
        self.assertEqual(self.avl.print(20), "C A")
        self.assertEqual(self.avl.print(25), "D C A")
        self.assertEqual(self.avl.print(30), "C A")
