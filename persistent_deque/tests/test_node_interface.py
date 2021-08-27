import unittest

from persistent_deque.node import Node
from persistent_deque.node.interface import Depth, AddLeaf

class NodeInterfaceTest(unittest.TestCase):
  def test_depth(self):
    self.assertEqual(Depth(Node(4, None, 10)), 10)
    self.assertEqual(Depth(None), -1)

    self.assertRaises(TypeError, lambda: Depth('invalid'))

  def test_add_leaf(self):
    root = Node(0, None, 0)
    node = AddLeaf(1, root)

    self.assertEqual(node.value, 1)
    self.assertEqual(node.parent, root)
    self.assertEqual(node.depth, 1)

  def test_add_leaf_none(self):
    node = AddLeaf(1, None)

    self.assertEqual(node.value, 1)
    self.assertEqual(node.parent, None)
    self.assertEqual(node.depth, 0)
    self.assertEqual(node.jump, None)

  def test_jump(self):
    root = AddLeaf(0, None)
    node1 = AddLeaf(1, root)
    node2 = AddLeaf(2, node1)
    node3 = AddLeaf(3, node2)
    node4 = AddLeaf(4, node3)
    node5 = AddLeaf(5, node4)

    self.assertEqual(root.jump, None)
    self.assertEqual(node1.jump, root)
    self.assertEqual(node2.jump, None)
    self.assertEqual(node3.jump, node2)
    self.assertEqual(node4.jump, node3)
    self.assertEqual(node5.jump, node2)