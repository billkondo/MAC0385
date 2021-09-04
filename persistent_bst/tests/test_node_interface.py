import unittest

from persistent_bst.node.node import Node
from persistent_bst.node.interface import CopyNode, InsertNode, MinNode, \
  SearchNode, DeleteNode, PrintNode

class NodeInterfaceTest(unittest.TestCase):
  def setUp(self):
    self.root = InsertNode(InsertNode(InsertNode(InsertNode(None,2),1),4),3)

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

  def test_search_node(self):
    self.assertRaises(TypeError, lambda: SearchNode('invalid', 5))
    self.assertRaises(ValueError, lambda: SearchNode(Node(5), None))

    root = InsertNode(InsertNode(InsertNode(None,3),2),1)

    self.assertTrue(SearchNode(root,1))
    self.assertTrue(SearchNode(root,2))
    self.assertTrue(SearchNode(root,3))

    self.assertFalse(SearchNode(root,4))
    self.assertFalse(SearchNode(root,0))

  def test_delete_node(self):
    self.assertRaises(ValueError, lambda: DeleteNode(None, 5))
    self.assertRaises(TypeError, lambda: DeleteNode('invalid', 5))
    self.assertRaises(ValueError, lambda: DeleteNode(Node(5), None))
    
    root1 = DeleteNode(self.root, 2)
    self.assertEqual(root1.value, 3)
    self.assertEqual(root1.right.value, 4)
    self.assertEqual(root1.left.value, 1)
    self.assertEqual(root1.left, self.root.left)
    self.assertNotEqual(root1.right, self.root.right)
    self.assertFalse(SearchNode(root1, 2))

  def test_print_node(self):
    self.assertEqual(PrintNode(self.root), "2 1 4 3")