import unittest
from unittest.mock import Mock

from retroactive_stack.bst.bst import BST
from retroactive_stack.interface import NewStack


class InterfaceTest(unittest.TestCase):
    def test_new_stack(self):
        bst = Mock(BST)
        self.assertEqual(NewStack(bst).bst, bst)
        self.assertIsInstance(NewStack().bst, BST)
