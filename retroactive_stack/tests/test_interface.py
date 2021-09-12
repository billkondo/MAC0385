import unittest
from unittest.mock import Mock

from retroactive_stack.bst.bst import BST
from retroactive_stack.interface import AddPop, AddPush, NewStack


class InterfaceTest(unittest.TestCase):
    def test_new_stack(self):
        bst = Mock(BST)
        self.assertEqual(NewStack(bst).bst, bst)
        self.assertIsInstance(NewStack().bst, BST)

    def test_add_push(self):
        self.assertRaises(TypeError, lambda: AddPush(None, 3, "A"))
        self.assertRaises(TypeError, lambda: AddPush("invalid", 1, "B"))
        self.assertRaises(
            TypeError,
            lambda: AddPush(NewStack(), "invalid", "C"),
        )

        bst = Mock(BST)
        stack = NewStack(bst)

        AddPush(stack, 5, "A")

        bst.insert.assert_called_once()

    def test_add_pop(self):
        bst = Mock(BST)
        stack = NewStack(bst)

        AddPop(stack, 10)

        bst.insert.assert_called_once()
