import unittest
from unittest.mock import Mock

from avl.avl_node import AVLNode, Height


class TestAVLNode(unittest.TestCase):
    def test_avl_node(self):
        self.assertRaises(TypeError, lambda: AVLNode())
        self.assertRaises(TypeError, lambda: AVLNode("invalid"))

        node = AVLNode(key=5)

        self.assertEqual(node.key, 5)
        self.assertEqual(node.min_key, 5)
        self.assertEqual(node.L, None)
        self.assertEqual(node.R, None)
        self.assertEqual(node.height, 0)
        self.assertEqual(node.balance, 0)

    def test_height(self):
        self.assertRaises(TypeError, lambda: Height("invalid"))

        self.assertEqual(Height(None), -1)

        node = AVLNode(key=1)
        node.height = 5
        self.assertEqual(Height(node), 5)

    def test_update(self):
        node = AVLNode(key=10)

        L = Mock(spec=AVLNode)
        L.min_key = 2
        L.height = 4
        node.L = L

        R = Mock(spec=AVLNode)
        R.min_key = 10
        R.height = 5
        node.R = R

        node.update()
        self.assertEqual(node.min_key, 2)
        self.assertEqual(node.height, 6)
        self.assertEqual(node.balance, 1)

    def test_update_left_empty(self):
        node = AVLNode(key=10)

        R = Mock(spec=AVLNode)

        R.min_key = 14
        R.height = 2
        node.R = R

        node.update()
        self.assertEqual(node.min_key, 10)
        self.assertEqual(node.height, 3)
        self.assertEqual(node.balance, 3)

    def test_update_right_empty(self):
        node = AVLNode(key=10)

        L = Mock(spec=AVLNode)
        L.min_key = 2
        L.height = 4
        node.L = L

        node.update()
        self.assertEqual(node.min_key, 2)
        self.assertEqual(node.height, 5)
        self.assertEqual(node.balance, -5)

    def test_update_leaf(self):
        node = AVLNode(key=10)

        node.height = 2
        node.balance = 2

        node.update()
        self.assertEqual(node.min_key, 10)
        self.assertEqual(node.height, 0)
        self.assertEqual(node.balance, 0)
