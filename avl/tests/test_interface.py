import unittest
from math import inf
from typing import Dict

from avl.avl_node import AVLNode, Height
from avl.interface import (
    Balance,
    Delete,
    Find,
    Insert,
    Min,
    RotateLeft,
    RotateRight,
)


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

    def test_min(self):
        self.assertRaises(TypeError, lambda: Min("invalid"))

        node10 = AVLNode(key=10)
        node5 = AVLNode(key=5)
        node15 = AVLNode(key=15)
        node12 = AVLNode(key=12)

        root = Insert(None, node10)
        root = Insert(root, node5)
        root = Insert(root, node15)
        root = Insert(root, node12)

        self.assertEqual(Min(root).key, 5)
        self.assertEqual(Min(node5).key, 5)
        self.assertEqual(Min(node15).key, 12)
        self.assertEqual(Min(node12).key, 12)

    def test_insert_delete_find(self):
        self.assertRaises(TypeError, lambda: Insert("invalid", AVLNode(key=5)))
        self.assertRaises(TypeError, lambda: Insert(AVLNode(key=5), "invalid"))
        self.assertRaises(TypeError, lambda: Delete("invalid"))
        self.assertRaises(TypeError, lambda: Find("invalid", 5))

        def count(node: AVLNode):
            if node is None:
                return 0

            return count(node.L) + 1 + count(node.R)

        def check_tree(root: AVLNode):
            height: Dict[AVLNode, int] = {}
            height[None] = -1

            balance: Dict[AVLNode, int] = {}
            balance[None] = 0

            def compute(node: AVLNode):
                if node is None:
                    return

                compute(node.L)
                compute(node.R)

                height[node] = max(height[node.L], height[node.R]) + 1
                balance[node] = balance[node.R] - balance[node.R]

            def check(node: AVLNode, left_key=-inf, right_key=inf):
                if node is None:
                    return

                if height[node] != Height(node):
                    raise ValueError("unmatched height")

                if balance[node] != Balance(node):
                    raise ValueError("unmatched balance")

                if node.key < left_key or right_key < node.key:
                    raise ValueError("BST invariant broken")

                if balance[node] < -1 or balance[node] > 1:
                    raise ValueError("AVL invariant broken")

                check(node.L, left_key, node.key)
                check(node.R, node.key, right_key)

            compute(root)

        def insert(root: AVLNode, key: int):
            self.assertIsNone(Find(root, key))
            root = Insert(root, AVLNode(key))
            self.assertEqual(Find(root, key).key, key)

            return root

        def delete(root: AVLNode, key: int):
            self.assertEqual(Find(root, key).key, key)
            root = Delete(root, key)
            self.assertIsNone(Find(root, key))

            return root

        root = None
        for key in range(1, 100):
            root = insert(root, key)

            self.assertEqual(count(root), key)
            check_tree(root)

        for key in range(1, 100):
            root = delete(root, key)

            self.assertEqual(count(root), 99 - key)
            check_tree(root)

        self.assertIsNone(root)

        for key in range(999, 0, -1):
            root = insert(root, key)

            self.assertEqual(count(root), 999 - key + 1)
            check_tree(root)

        size = 999
        for key in range(999, 1, -5):
            root = delete(root, key)
            size -= 1

            self.assertEqual(count(root), size)
            check_tree(root)
