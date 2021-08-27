from typing import Type
import unittest

from persistent_deque.node import Node
from persistent_deque.node.interface import Depth, AddLeaf \
  ,LevelAncestor 

class NodeInterfaceTest(unittest.TestCase):
  def setUp(self):
    self.root = AddLeaf(0, None)
    self.node1 = AddLeaf(1, self.root)
    self.node2 = AddLeaf(2, self.node1)
    self.node3 = AddLeaf(3, self.node2)
    self.node4 = AddLeaf(4, self.node3)
    self.node5 = AddLeaf(5, self.node4)

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
    self.assertEqual(self.root.jump, None)
    self.assertEqual(self.node1.jump, self.root)
    self.assertEqual(self.node2.jump, None)
    self.assertEqual(self.node3.jump, self.node2)
    self.assertEqual(self.node4.jump, self.node3)
    self.assertEqual(self.node5.jump, self.node2)

  def test_level_ancestor(self):
    self.assertEqual(LevelAncestor(0, self.root), self.root)
    self.assertEqual(LevelAncestor(4, self.node5), self.node1)
    self.assertEqual(LevelAncestor(3, self.node4), self.node1)
    self.assertEqual(LevelAncestor(2, self.node2), self.root)
    self.assertEqual(LevelAncestor(5, self.node5), self.root)
    self.assertEqual(LevelAncestor(3, self.node5), self.node2)

  def test_level_ancestor_raises(self):
    self.assertRaises(TypeError, lambda: LevelAncestor('invalid', None))
    self.assertRaises(ValueError, lambda: LevelAncestor(0, None))
    self.assertRaises(TypeError, lambda: LevelAncestor(0, 'invalid'))
    self.assertRaises(ValueError, lambda: LevelAncestor(10, self.node5))