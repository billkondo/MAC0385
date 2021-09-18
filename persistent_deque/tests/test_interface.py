import unittest

from persistent_deque.deque import Deque
from persistent_deque.interface import (
    Back,
    Front,
    Kth,
    NewDeque,
    PopBack,
    PopFront,
    Print,
    PushBack,
    PushFront,
    Swap,
)
from persistent_deque.node.node import Node


class InterfaceTest(unittest.TestCase):
    def setUp(self):
        self.node1 = Node(1, None, 0)
        self.node2 = Node(2, None, 0)
        self.deque = Deque(self.node1, self.node2)

    def test_new_deque(self):
        deque = NewDeque()

        self.assertEqual(deque.first, None)
        self.assertEqual(deque.last, None)

    def test_front(self):
        self.assertEqual(Front(self.deque), self.node1.value)

        self.assertRaises(TypeError, lambda: Front(None))
        self.assertRaises(TypeError, lambda: Front("invalid"))

    def test_back(self):
        self.assertEqual(Back(self.deque), self.node2.value)

        self.assertRaises(TypeError, lambda: Back(None))
        self.assertRaises(TypeError, lambda: Back("invalid"))

    def test_push_front(self):
        new_deque = PushFront(self.deque, 3)
        new_deque_first = new_deque.first

        self.assertEqual(new_deque.last, self.node2)

        self.assertEqual(new_deque_first.value, 3)
        self.assertEqual(new_deque_first.parent, self.node1)
        self.assertEqual(new_deque_first.depth, 1)

        self.assertRaises(TypeError, lambda: PushFront(None, 3))
        self.assertRaises(TypeError, lambda: PushFront("invalid", 3))

    def test_push_front_emtpy(self):
        new_deque = PushFront(NewDeque(), 1)

        self.assertEqual(new_deque.first, new_deque.last)

        self.assertEqual(new_deque.first.value, 1)
        self.assertEqual(new_deque.first.parent, new_deque.first)
        self.assertEqual(new_deque.first.depth, 0)

    def test_swap(self):
        deque_swap = Swap(self.deque)

        self.assertEqual(deque_swap.first, self.node2)
        self.assertEqual(deque_swap.last, self.node1)

        self.assertRaises(TypeError, lambda: Swap(None))
        self.assertRaises(TypeError, lambda: Swap("invalid"))

    def test_push_back(self):
        new_deque = PushBack(self.deque, 3)
        new_deque_last = new_deque.last

        self.assertEqual(new_deque.first, self.node1)

        self.assertEqual(new_deque_last.value, 3)
        self.assertEqual(new_deque_last.parent, self.node2)
        self.assertEqual(new_deque_last.depth, 1)

        self.assertRaises(TypeError, lambda: PushBack(None, 3))
        self.assertRaises(TypeError, lambda: PushBack("invalid", 3))

    def test_push_back_empty(self):
        new_deque = PushBack(NewDeque(), 1)

        self.assertEqual(new_deque.first, new_deque.last)

        self.assertEqual(new_deque.first.value, 1)
        self.assertEqual(new_deque.first.parent, new_deque.first)
        self.assertEqual(new_deque.first.depth, 0)


class PopInterfaceTest(unittest.TestCase):
    def setUp(self):
        self.root = NewDeque()

        self.deque1 = PushFront(self.root, 1)
        self.node1 = self.deque1.first

        self.deque2 = PushFront(self.deque1, 2)
        self.node2 = self.deque2.first

        self.deque3 = PushFront(self.deque2, 3)
        self.node3 = self.deque3.first

        self.deque4 = PushBack(self.deque3, 4)
        self.node4 = self.deque4.last

        self.deque5 = PushBack(self.deque4, 5)
        self.node5 = self.deque5.last

    def test_kth(self):
        self.assertEqual(Kth(self.deque5, 1), 3)
        self.assertEqual(Kth(self.deque5, 2), 2)
        self.assertEqual(Kth(self.deque5, 3), 1)
        self.assertEqual(Kth(self.deque5, 4), 4)
        self.assertEqual(Kth(self.deque5, 5), 5)

        self.assertEqual(Kth(self.deque1, 1), 1)
        self.assertEqual(Kth(self.deque2, 2), 1)

    def test_kth_raises(self):
        self.assertRaises(ValueError, lambda: Kth(self.deque5, 6))
        self.assertRaises(ValueError, lambda: Kth(self.deque4, 5))
        self.assertRaises(TypeError, lambda: Kth(None, 1))
        self.assertRaises(TypeError, lambda: Kth("invalid", 1))
        self.assertRaises(TypeError, lambda: Kth(self.deque2, "invalid"))
        self.assertRaises(ValueError, lambda: Kth(self.deque5, -1))

    def test_pop_front(self):
        deque6 = PopFront(self.deque5)
        self.assertEqual(deque6.first, self.node2)
        self.assertEqual(deque6.last, self.node5)

        deque7 = PopFront(self.deque1)
        self.assertEqual(deque7.first, None)
        self.assertEqual(deque7.last, None)

        deque8 = PopFront(PopFront(deque6))
        self.assertEqual(deque8.first, self.node4)
        self.assertEqual(deque8.last, self.node5)

    def test_pop_front_raises(self):
        self.assertRaises(TypeError, lambda: PopFront(None))
        self.assertRaises(TypeError, lambda: PopFront("invalid"))

        self.assertRaises(ValueError, lambda: PopFront(self.root))

    def test_pop_back(self):
        deque6 = PopBack(self.deque5)
        self.assertEqual(deque6.first, self.node3)
        self.assertEqual(deque6.last, self.node4)

        deque7 = PopBack(self.deque3)
        self.assertEqual(deque7.first, self.node3)
        self.assertEqual(deque7.last, self.node2)

        deque8 = PopBack(self.deque1)
        self.assertEqual(deque8.first, None)
        self.assertEqual(deque8.last, None)

    def test_pop_back_raises(self):
        self.assertRaises(TypeError, lambda: PopBack(None))
        self.assertRaises(TypeError, lambda: PopBack("invalid"))

        self.assertRaises(ValueError, lambda: PopBack(self.root))


class PrintInterfaceTest(unittest.TestCase):
    def setUp(self):
        self.root = NewDeque()
        self.deque1 = PushFront(self.root, 1)
        self.deque2 = PushFront(self.deque1, 2)
        self.deque3 = PushFront(self.deque2, 3)
        self.deque4 = PushBack(self.deque3, 4)
        self.deque5 = PushBack(self.deque4, 5)
        self.deque6 = PopFront(self.deque5)
        self.deque7 = PopFront(self.deque6)
        self.deque8 = PushFront(self.deque7, 6)
        self.deque9 = PopBack(self.deque8)
        self.deque10 = PushBack(self.deque9, 7)

    def test_print(self):
        self.assertEqual(Print(self.root), "")
        self.assertEqual(Print(self.deque8), "6 1 4 5")
        self.assertEqual(Print(self.deque3), "3 2 1")
        self.assertEqual(Print(self.deque5), "3 2 1 4 5")
        self.assertEqual(Print(self.deque1), "1")
        self.assertEqual(Print(self.deque10), "6 1 4 7")
        self.assertEqual(Print(self.deque7), "1 4 5")

    def test_print_raises(self):
        self.assertRaises(TypeError, lambda: Print(None))
        self.assertRaises(TypeError, lambda: Print("invalid"))
