import unittest
from unittest.mock import Mock

from retroactive_stack.bst.bst import BST
from retroactive_stack.interface import (
    AddPop,
    AddPush,
    Delete,
    Kth,
    NewStack,
    Top,
)


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

    def test_delete(self):
        bst = Mock(BST)
        stack = NewStack(bst)

        Delete(stack, 10)

        bst.delete.assert_called_with(10)

    def test_kth(self):
        bst = Mock(BST)
        bst.kth.return_value = "A"
        stack = NewStack(bst)

        self.assertEqual(
            Kth(stack, 10, 5),
            "A",
        )

        bst.kth.assert_called_with(
            key=10,
            k=5,
        )

    def test_top(self):
        bst = Mock(BST)
        bst.kth.return_value = "A"
        stack = NewStack(bst)

        self.assertEqual(
            Top(stack, 20),
            "A",
        )

        bst.kth.assert_called_with(
            key=20,
            k=1,
        )
