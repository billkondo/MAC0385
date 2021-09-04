from typing import Any, List
import unittest

from persistent_bst.bst import BST
from persistent_bst.interface import NewBST, Insert, Delete, Search, \
  Min, Print

class PersistentBSTTester():
  def __init__(self):
    self.bsts: List[BST] = []

  def NewBST(self):
    self.bsts.append(NewBST())

  def Insert(self, t: int, value):
    self.bsts.append(Insert(self.bsts[t], value))

  def Delete(self, t: int, value):
    self.bsts.append(Delete(self.bsts[t], value))

  def Search(self, t: int, value) -> bool:
    return Search(self.bsts[t], value)
  
  def Min(self, t: int) -> Any:
    return Min(self.bsts[t])

  def Print(self, t: int) -> str:
    return Print(self.bsts[t])

class PersistentBSTTest(unittest.TestCase):
  def test_1(self):
    tester = PersistentBSTTester()

    tester.NewBST()
    self.assertEqual(tester.Print(0), "")

    tester.Insert(0, 7)
    self.assertEqual(tester.Print(1), "7")

    tester.Insert(1, 10)
    self.assertEqual(tester.Print(2), "7 10")

    tester.Insert(2, 5)
    self.assertEqual(tester.Print(3), "7 5 10")

    tester.Insert(3, 6)
    self.assertEqual(tester.Print(4), "7 5 6 10")
    self.assertEqual(tester.Min(4), 5)

    tester.Insert(4, 4)
    self.assertEqual(tester.Print(5), "7 5 4 6 10")
    self.assertTrue(tester.Search(5, 6))

    tester.Delete(4, 5)
    self.assertEqual(tester.Print(6), "7 6 10")

    tester.Insert(6, 4)
    self.assertEqual(tester.Print(7), "7 6 4 10")
    self.assertEqual(tester.Min(7), 4)

    tester.Insert(5, 8)
    self.assertEqual(tester.Print(8), "7 5 4 6 10 8")

    tester.Insert(8, 12)
    self.assertEqual(tester.Print(9), "7 5 4 6 10 8 12")

    tester.Delete(9, 7)
    self.assertEqual(tester.Print(10), "8 5 4 6 10 12")

    tester.Delete(10, 5)
    self.assertEqual(tester.Print(11), "8 6 4 10 12")

    tester.Delete(11, 4)
    self.assertEqual(tester.Print(12), "8 6 10 12")