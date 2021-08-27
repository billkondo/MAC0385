import unittest

from persistent_deque.node import Node
from persistent_deque.deque import Deque
from persistent_deque.interface import NewDeque, Front, Back, PushFront

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

  def test_back(self):
    self.assertEqual(Back(self.deque), self.node2.value)

  def test_push_front(self):
    new_deque = PushFront(self.deque, 3)
    new_deque_first = new_deque.first

    self.assertEqual(new_deque.last, self.node2)

    self.assertEqual(new_deque_first.value, 3)
    self.assertEqual(new_deque_first.parent, self.node1)
    self.assertEqual(new_deque_first.depth, self.node1.depth + 1)

  def test_push_front_emtpy(self):
    new_deque = PushFront(NewDeque(), 1)

    self.assertEqual(new_deque.first, new_deque.last)

    self.assertEqual(new_deque.first.value, 1)
    self.assertEqual(new_deque.first.parent, None)
    self.assertEqual(new_deque.first.depth, 0)