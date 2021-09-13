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

    def test_constructor(self):
        avl = AVL()
        self.assertIsNone(avl.root)

    def test_insert(self):
        avl = AVL()

        for idx, op in enumerate(self.operations):
            avl.insert(idx, op)

        self.assertEqual(Sum(avl.root), 2)
