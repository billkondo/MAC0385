import unittest

from retroactive_stack.interface import (
    AddPop,
    AddPush,
    Delete,
    Kth,
    NewStack,
    Print,
    Size,
    Top,
)


class ReatroactiveStackTest(unittest.TestCase):
    def test_with_simple_bst(self):
        stack = NewStack()

        AddPush(stack, 10, "A")
        AddPush(stack, 20, "C")
        AddPush(stack, 30, "F")

        self.assertEqual(Print(stack, 30), "F C A")
        self.assertEqual(Top(stack, 25), "C")
        self.assertEqual(Kth(stack, 29, 2), "A")

        AddPop(stack, 25)

        self.assertEqual(Print(stack, 30), "F A")
        self.assertEqual(Kth(stack, 25, 1), "A")
        self.assertEqual(Top(stack, 24), "C")

        AddPush(stack, 15, "D")

        self.assertEqual(Print(stack, 30), "F D A")
        self.assertEqual(Kth(stack, 30, 3), "A")

        AddPop(stack, 19)

        self.assertEqual(Print(stack, 30), "F A")
        self.assertEqual(Size(stack, 29), 1)

        AddPush(stack, 5, "Z")
        Delete(stack, 10)

        self.assertEqual(Print(stack, 30), "F Z")
        self.assertEqual(Print(stack, 22), "C Z")
        self.assertEqual(Size(stack, 22), 2)
        self.assertEqual(Size(stack, 25), 1)
