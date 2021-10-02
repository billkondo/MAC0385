import unittest

from avl.avl_node import AVLNode
from avl.interface import Balance, RotateLeft, RotateRight


class TestInterface(unittest.TestCase):
    def test_rotate_right(self):
        self.assertRaises(TypeError, lambda: RotateRight(None))

        node_no_left_child = AVLNode(key=10)
        self.assertEqual(RotateRight(node_no_left_child), node_no_left_child)

        x = AVLNode(key=10)
        y = AVLNode(key=5)
        t1 = AVLNode(key=2)
        t2 = AVLNode(key=4)
        t3 = AVLNode(key=11)

        y.update()
        x.update()

        x.L = y
        x.R = t3
        y.L = t1
        y.R = t2

        node = RotateRight(x)
        self.assertEqual(node, y)
        self.assertEqual(node.R, x)
        self.assertEqual(node.L, t1)
        self.assertEqual(x.L, t2)
        self.assertEqual(x.R, t3)

        self.assertEqual(y.min_key, 2)
        self.assertEqual(y.height, 2)
        self.assertEqual(y.balance, 1)

        self.assertEqual(x.min_key, 4)
        self.assertEqual(x.height, 1)

    def test_rotate_left(self):
        self.assertRaises(TypeError, lambda: RotateLeft("invalid"))

        node_no_right_child = AVLNode(key=10)
        self.assertEqual(RotateLeft(node_no_right_child), node_no_right_child)

        y = AVLNode(10)
        x = AVLNode(15)
        t1 = AVLNode(5)
        t2 = AVLNode(12)
        t3 = AVLNode(20)

        y.L = t1
        y.R = x

        x.L = t2
        x.R = t3

        x.update()
        y.update()

        node = RotateLeft(y)
        self.assertEqual(node, x)
        self.assertEqual(node.L, y)
        self.assertEqual(node.R, t3)
        self.assertEqual(y.L, t1)
        self.assertEqual(y.R, t2)

        self.assertEqual(x.min_key, 5)
        self.assertEqual(x.height, 2)
        self.assertEqual(x.balance, -1)

        self.assertEqual(y.min_key, 5)
        self.assertEqual(y.height, 1)

    def test_balance(self):
        self.assertRaises(TypeError, lambda: Balance("invalid"))

        x = AVLNode(10)
        xL = AVLNode(5)
        xR = AVLNode(15)
        xLL = AVLNode(0)

        x.L = xL
        x.R = xR
        xL.L = xLL

        xL.update()
        x.update()

        node = Balance(x)
        self.assertEqual(node, x)
        self.assertEqual(node.L, xL)
        self.assertEqual(node.R, xR)
        self.assertEqual(xL.L, xLL)

    def test_balance_left(self):
        x = AVLNode(10)
        xL = AVLNode(5)
        xLL = AVLNode(0)

        x.L = xL
        xL.L = xLL

        xL.update()
        x.update()

        node = Balance(x)
        self.assertEqual(node, xL)
        self.assertEqual(node.R, x)
        self.assertEqual(node.L, xLL)

    def test_balance_left_right(self):
        x = AVLNode(10)
        xL = AVLNode(5)
        xLR = AVLNode(8)

        x.L = xL
        xL.R = xLR

        xL.update()
        x.update()

        node = Balance(x)
        self.assertEqual(node, xLR)
        self.assertEqual(node.L, xL)
        self.assertEqual(node.R, x)

    def test_balance_right(self):
        x = AVLNode(10)
        xR = AVLNode(15)
        xRR = AVLNode(20)

        x.R = xR
        xR.R = xRR

        xR.update()
        x.update()

        node = Balance(x)
        self.assertEqual(node, xR)
        self.assertEqual(node.L, x)
        self.assertEqual(node.R, xRR)

    def test_balance_right_left(self):
        x = AVLNode(10)
        xR = AVLNode(15)
        xRL = AVLNode(12)

        x.R = xR
        xR.L = xRL

        xR.update()
        x.update()

        node = Balance(x)
        self.assertEqual(node, xRL)
        self.assertEqual(node.L, x)
        self.assertEqual(node.R, xR)
