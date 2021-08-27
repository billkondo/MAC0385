import unittest

from persistent_deque.interface import NewDeque

class InterfaceTest(unittest.TestCase):
  def test_new_deque(self):
    deque = NewDeque()

    self.assertEqual(deque.first, None)
    self.assertEqual(deque.last, None)