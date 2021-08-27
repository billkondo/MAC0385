import unittest

from persistent_deque.node import Node
from persistent_deque.deque import Deque
from persistent_deque.interface import NewDeque, Front, Back

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