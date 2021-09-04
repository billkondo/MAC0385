import unittest

from persistent_bst.node.node import Node
from persistent_bst.node.interface import CopyNode, InsertNode, MinNode

class NodeInterfaceTest(unittest.TestCase):
  def test_copy_node(self):
    self.assertRaises(TypeError, lambda: CopyNode('invalid'))

    node = Node(5)
    node.left = Node(4)
    node.right = Node(7)

    copy_node = CopyNode(node)

    self.assertEqual(copy_node.left, node.left)
    self.assertEqual(copy_node.right, node.right)
    self.assertEqual(copy_node.value, node.value)
    self.assertNotEqual(copy_node, node)

  def test_insert_node(self):
    self.assertRaises(TypeError, lambda: InsertNode('invalid', 5))
    self.assertRaises(ValueError, lambda: InsertNode(Node(1), None))

    new_node = InsertNode(None, 5)
    self.assertEqual(new_node.value, 5)

    root = Node(10)
    root_right = InsertNode(root, 15)
    self.assertEqual(root_right.right.value, 15)
    self.assertNotEqual(root, root_right)
    
    root_left = InsertNode(root, 5)
    self.assertEqual(root_left.left.value, 5)
    self.assertNotEqual(root, root_left)

  def test_min_node(self):
    self.assertRaises(ValueError, lambda: MinNode(None))
    self.assertRaises(TypeError, lambda: MinNode('invalid'))

    root1 = InsertNode(InsertNode(None, 5), 10)
    self.assertEqual(MinNode(root1).value, 5)

    root2 = InsertNode(InsertNode(None, 20), 10)
    self.assertEqual(MinNode(root2).value, 10)