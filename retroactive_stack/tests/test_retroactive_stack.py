import unittest
from time import process_time

from retroactive_stack.bst.avl.avl import AVL
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
from retroactive_stack.stack import Stack


class ReatroactiveStackTest(unittest.TestCase):
    def run_test_01(self, stack: Stack):
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

    def test_with_simple_bst_01(self):
        stack = NewStack()
        self.run_test_01(stack)

    def test_with_avl_01(self):
        stack = NewStack(AVL())
        self.run_test_01(stack)

    def test_wit_avl_02(self):
        stack_avl = NewStack(AVL())
        stack = NewStack()

        def compare(time: int):
            size = Size(stack, time)
            self.assertEqual(Size(stack_avl, time), size)
            self.assertEqual(Top(stack_avl, time), Top(stack, time))
            self.assertEqual(Print(stack, time), Print(stack_avl, time))

            for k in range(1, size + 1):
                self.assertEqual(Kth(stack, time, k), Kth(stack_avl, time, k))

        self.assertEqual(Size(stack_avl, 100), 0)
        self.assertEqual(Size(stack_avl, 100), 0)

        for time in range(1, 100):
            if time % 10 == 0:
                AddPop(stack_avl, time)
                AddPop(stack, time)
            else:
                AddPush(stack_avl, time, time)
                AddPush(stack, time, time)

            compare(time)

        for time in range(1, 100):
            compare(time)

        for time in range(5, 100, 4):
            Delete(stack, time)
            Delete(stack_avl, time)

            compare(time)

    def test_avl_stress(self):
        start_time = process_time()
        time_limit = 2.0

        stack = NewStack(AVL())
        for i in range(0, 10000):
            AddPush(stack, i, i)

            if process_time() - start_time > time_limit:
                raise TimeoutError("Time limit exceeded")

        for i in range(0, 10000):
            Delete(stack, i)

            if process_time() - start_time > time_limit:
                raise TimeoutError("Time limit exceeded")

        duration = process_time() - start_time

        self.assertLessEqual(duration, time_limit)
