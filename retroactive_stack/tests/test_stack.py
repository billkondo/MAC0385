import unittest

from retroactive_stack.bst.simple_bst import SimpleBST
from retroactive_stack.stack import Stack


class StackTest(unittest.TestCase):
    def test_constructor(self):
        self.assertRaises(TypeError, lambda: Stack(bst="invalid"))

        bst = SimpleBST()
        stack = Stack(bst=bst)

        self.assertEqual(bst, stack.bst)

        self.assertIsInstance(Stack().bst, SimpleBST)
