import time
import unittest
from typing import List

from persistent_deque.deque import Deque
from persistent_deque.interface import (
    Kth,
    NewDeque,
    PopBack,
    PopFront,
    Print,
    PushBack,
    PushFront,
)


class PersistentDequeTester:
    def __init__(self):
        self.deques: List[Deque] = []

    def NewDeque(self):
        self.deques.append(NewDeque())

    def Front(self, t: int) -> str:
        return self.deques[t].first.value

    def Back(self, t: int) -> str:
        return self.deques[t].last.value

    def PushFront(self, t: int, value: int):
        self.deques.append(PushFront(self.deques[t], value))

    def PushBack(self, t: int, value: int):
        self.deques.append(PushBack(self.deques[t], value))

    def PopFront(self, t: int):
        self.deques.append(PopFront(self.deques[t]))

    def PopBack(self, t: int):
        self.deques.append(PopBack(self.deques[t]))

    def Kth(self, t: int, k: int):
        return Kth(self.deques[t], k)

    def Print(self, t: int):
        return Print(self.deques[t])


class PersistentDequeTest(unittest.TestCase):
    def test_1(self):
        tester = PersistentDequeTester()

        tester.NewDeque()
        tester.PushFront(0, 1)
        tester.PushFront(1, 2)
        tester.PushBack(1, 3)
        tester.PushBack(3, 4)
        self.assertEqual(tester.Print(4), "1 3 4")
        self.assertEqual(tester.Kth(4, 2), 3)
        tester.PushFront(4, 5)
        tester.PushBack(2, 6)
        self.assertEqual(tester.Front(6), 2)
        tester.PushFront(6, 7)
        self.assertEqual(tester.Kth(7, 4), 6)
        self.assertEqual(tester.Print(5), "5 1 3 4")
        self.assertEqual(tester.Print(7), "7 2 1 6")
        tester.PopBack(6)
        self.assertEqual(tester.Print(8), "2 1")
        tester.PopFront(8)
        self.assertEqual(tester.Front(9), 1)

    def test_2(self):
        tester = PersistentDequeTester()

        tester.NewDeque()
        tester.PushBack(0, 1)
        tester.PushBack(1, 2)
        tester.PushBack(2, 3)
        tester.PushBack(3, 4)
        tester.PushBack(4, 5)
        tester.PushBack(5, 6)
        tester.PushBack(6, 7)
        tester.PushBack(7, 8)
        tester.PushBack(8, 9)
        self.assertEqual(tester.Print(9), "1 2 3 4 5 6 7 8 9")
        tester.PopFront(9)
        tester.PopFront(10)
        self.assertEqual(tester.Kth(11, 5), 7)
        tester.PopBack(11)
        tester.PopFront(12)
        self.assertEqual(tester.Front(13), 4)
        self.assertEqual(tester.Back(13), 8)
        tester.PopBack(13)
        self.assertEqual(tester.Print(14), "4 5 6 7")

    def test_stress(self):
        tester = PersistentDequeTester()
        start_time = time.process_time()
        time_limit = 5.0

        tester.NewDeque()
        for i in range(0, 100000):
            tester.PushBack(i, i + 1)

            if time.process_time() - start_time > time_limit:
                raise TimeoutError("Time limit exceeded")

        for i in range(0, 100000):
            tester.PopFront(100000 + i)

            if time.process_time() - start_time > time_limit:
                raise TimeoutError("Time limit exceeded")

        duration = time.process_time() - start_time

        self.assertLessEqual(duration, time_limit)

    def test_3(self):
        tester = PersistentDequeTester()

        tester.NewDeque()
        tester.PushFront(0, 1)
        self.assertEqual(tester.Kth(1, 1), 1)
        tester.PopFront(1)
        self.assertEqual(tester.Print(2), "")
        tester.PushFront(1, 2)
        tester.PushFront(3, 3)
        tester.PopBack(4)
        tester.PushBack(5, 4)
        self.assertEqual(tester.Kth(6, 3), 4)
        tester.PushBack(3, 5)
        tester.PushBack(7, 6)
        tester.PushBack(8, 7)
        self.assertEqual(tester.Print(9), "2 1 5 6 7")
