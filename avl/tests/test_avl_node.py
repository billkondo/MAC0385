import unittest

from avl.avl_node import AVLNode


class TestAVLNode(unittest.TestCase):
    def test_avl_node(self):
        self.assertRaises(TypeError, lambda: AVLNode())
        self.assertRaises(TypeError, lambda: AVLNode('invalid'))

        node = AVLNode(key=5)

        self.assertEqual(node.key, 5)
        self.assertEqual(node.height, 0)
        self.assertEqual(node.balance, 0)
