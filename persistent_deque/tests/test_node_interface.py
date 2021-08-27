import unittest

from persistent_deque.node import Node
from persistent_deque.node.interface import Depth

class NodeInterfaceTest(unittest.TestCase):
  def test_depth(self):
    self.assertEqual(Depth(Node(4, None, 10)), 10)

    self.assertRaises(ValueError, lambda: Depth(None))
    self.assertRaises(TypeError, lambda: Depth('invalid'))