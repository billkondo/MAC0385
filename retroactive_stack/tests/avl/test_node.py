import unittest
from math import inf
from unittest.mock import Mock

from retroactive_stack.bst.avl.node import (
    Balance,
    Height,
    Max,
    Min,
    Node,
    RotateLeft,
    RotateRight,
    Sum,
    Type,
    Update,
)
from retroactive_stack.operation import Operation


class NodeTest(unittest.TestCase):
    def test_push_constructor(self):
        self.assertRaises(TypeError, lambda: Node())
        self.assertRaises(TypeError, lambda: Node(key=5))
        self.assertRaises(
            TypeError,
            lambda: Node(
                operation=Operation(
                    type=1,
                    value="A",
                ),
            ),
        )

        push_operation = Operation(type=1, value="A")
        push_node = Node(key=10, operation=push_operation)

        self.assertEqual(push_node.key, 10)
        self.assertEqual(push_node.min_key, 10)
        self.assertEqual(push_node.operation, push_operation)
        self.assertIsNone(push_node.L)
        self.assertIsNone(push_node.R)
        self.assertEqual(push_node.sum, 1)
        self.assertEqual(push_node.max, 1)
        self.assertEqual(push_node.min, 1)
        self.assertEqual(push_node.height, 0)
        self.assertEqual(push_node.balance, 0)

    def test_pop_constructor(self):
        pop_operation = Operation(type=-1)
        pop_node = Node(key=20, operation=pop_operation)

        self.assertEqual(pop_node.key, 20)
        self.assertEqual(pop_node.min_key, 20)
        self.assertEqual(pop_node.operation, pop_operation)
        self.assertIsNone(pop_node.L)
        self.assertIsNone(pop_node.R)
        self.assertEqual(pop_node.sum, -1)
        self.assertEqual(pop_node.max, -1)
        self.assertEqual(pop_node.min, -1)
        self.assertEqual(pop_node.height, 0)
        self.assertEqual(pop_node.balance, 0)

    def test_height(self):
        self.assertEqual(Height(None), -1)

        node = Node(
            key=10,
            operation=Operation(
                type=-1,
            ),
        )
        node.height = 5
        self.assertEqual(Height(node), 5)

    def test_max(self):
        self.assertRaises(TypeError, lambda: Max("invalid"))

        node = Node(
            key=1,
            operation=Operation(type=-1),
        )
        node.max = 10
        self.assertEqual(Max(node), 10)
        self.assertEqual(Max(None), -inf)

    def test_min(self):
        self.assertRaises(TypeError, lambda: Min("invalid"))

        node = Node(
            key=1,
            operation=Operation(type=-1),
        )
        node.min = 10
        self.assertEqual(Min(node), 10)
        self.assertEqual(Min(None), inf)

    def test_type(self):
        self.assertRaises(TypeError, lambda: Type(None))

        self.assertEqual(
            Type(
                Node(
                    key=10,
                    operation=Operation(
                        type=1,
                        value="A",
                    ),
                ),
            ),
            1,
        )

    def test_sum(self):
        self.assertRaises(TypeError, lambda: Sum("invalid"))

        node = Node(
            key=10,
            operation=Operation(
                type=1,
                value="A",
            ),
        )
        node.sum = 10
        self.assertEqual(Sum(node), 10)
        self.assertEqual(Sum(None), 0)

    def test_update(self):
        self.assertRaises(TypeError, lambda: Update(None))

        node = Node(
            key=10,
            operation=Operation(
                type=1,
                value="A",
            ),
        )

        L = Mock(spec=Node)
        L.sum = 4
        L.max = 3
        L.min = 2
        L.min_key = 2
        L.height = 4
        node.L = L

        R = Mock(spec=Node)
        R.sum = -5
        R.max = 8
        R.min = -1
        R.min_key = 10
        R.height = 5
        node.R = R

        Update(node)
        self.assertEqual(node.sum, 0)
        self.assertEqual(node.max, 13)
        self.assertEqual(node.min, 2)
        self.assertEqual(node.min_key, 2)
        self.assertEqual(node.height, 6)
        self.assertEqual(node.balance, 1)

    def test_update_left_empty(self):
        node = Node(
            key=10,
            operation=Operation(
                type=-1,
            ),
        )

        R = Mock(spec=Node)
        R.sum = 5
        R.max = 2
        R.min = -2
        R.min_key = 14
        R.height = 2
        node.R = R

        Update(node)
        self.assertEqual(node.sum, 4)
        self.assertEqual(node.max, 1)
        self.assertEqual(node.min, -3)
        self.assertEqual(node.min_key, 10)
        self.assertEqual(node.height, 3)
        self.assertEqual(node.balance, 3)

    def test_update_right_empty(self):
        node = Node(
            key=10,
            operation=Operation(
                type=-1,
            ),
        )

        L = Mock(spec=Node)
        L.sum = 10
        L.max = 11
        L.min = 1
        L.min_key = 2
        L.height = 4
        node.L = L

        Update(node)
        self.assertEqual(node.sum, 9)
        self.assertEqual(node.max, 11)
        self.assertEqual(node.min, 1)
        self.assertEqual(node.min_key, 2)
        self.assertEqual(node.height, 5)
        self.assertEqual(node.balance, -5)

    def test_update_leaf(self):
        node = Node(
            key=10,
            operation=Operation(
                type=1,
                value="A",
            ),
        )

        node.height = 2
        node.balance = 2

        Update(node)
        self.assertEqual(node.sum, 1)
        self.assertEqual(node.max, 1)
        self.assertEqual(node.min_key, 10)
        self.assertEqual(node.height, 0)
        self.assertEqual(node.balance, 0)

    def test_rotate_right(self):
        self.assertRaises(TypeError, lambda: RotateRight(None))

        node_no_left_child = Node(
            key=10,
            operation=Operation(
                type=-1,
            ),
        )
        self.assertEqual(RotateRight(node_no_left_child), node_no_left_child)

        x = Node(key=10, operation=Operation(1, "A"))
        y = Node(key=5, operation=Operation(1, "B"))
        t1 = Node(key=2, operation=Operation(1, "C"))
        t2 = Node(key=4, operation=Operation(-1))
        t3 = Node(key=11, operation=Operation(-1))

        Update(y)
        Update(x)

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

        self.assertEqual(y.sum, 1)
        self.assertEqual(y.max, 2)
        self.assertEqual(y.height, 2)
        self.assertEqual(y.balance, 1)

        self.assertEqual(x.sum, -1)
        self.assertEqual(x.max, 0)
        self.assertEqual(x.height, 1)

    def test_rotate_left(self):
        self.assertRaises(TypeError, lambda: RotateLeft("invalid"))

        node_no_right_child = Node(
            key=10,
            operation=Operation(
                type=1,
                value="A",
            ),
        )
        self.assertEqual(RotateLeft(node_no_right_child), node_no_right_child)

        y = Node(10, Operation(1, "A"))
        x = Node(15, Operation(-1))
        t1 = Node(5, Operation(1, "C"))
        t2 = Node(12, Operation(1, "B"))
        t3 = Node(20, Operation(-1))

        y.L = t1
        y.R = x

        x.L = t2
        x.R = t3

        Update(x)
        Update(y)

        node = RotateLeft(y)
        self.assertEqual(node, x)
        self.assertEqual(node.L, y)
        self.assertEqual(node.R, t3)
        self.assertEqual(y.L, t1)
        self.assertEqual(y.R, t2)

        self.assertEqual(x.sum, 1)
        self.assertEqual(x.max, 3)
        self.assertEqual(x.height, 2)
        self.assertEqual(x.balance, -1)

        self.assertEqual(y.sum, 3)
        self.assertEqual(y.max, 3)
        self.assertEqual(y.height, 1)

    def test_balance(self):
        self.assertRaises(TypeError, lambda: Balance("invalid"))

        x = Node(10, Operation(1, "C"))
        xL = Node(5, Operation(1, "B"))
        xR = Node(15, Operation(-1))
        xLL = Node(0, Operation(1, "A"))

        x.L = xL
        x.R = xR
        xL.L = xLL

        Update(xL)
        Update(x)

        node = Balance(x)
        self.assertEqual(node, x)
        self.assertEqual(node.L, xL)
        self.assertEqual(node.R, xR)
        self.assertEqual(xL.L, xLL)

    def test_balance_left(self):
        x = Node(10, Operation(1, "C"))
        xL = Node(5, Operation(1, "B"))
        xLL = Node(0, Operation(1, "A"))

        x.L = xL
        xL.L = xLL

        Update(xL)
        Update(x)

        node = Balance(x)
        self.assertEqual(node, xL)
        self.assertEqual(node.R, x)
        self.assertEqual(node.L, xLL)

    def test_balance_left_right(self):
        x = Node(10, Operation(1, "C"))
        xL = Node(5, Operation(1, "A"))
        xLR = Node(8, Operation(1, "B"))

        x.L = xL
        xL.R = xLR

        Update(xL)
        Update(x)

        node = Balance(x)
        self.assertEqual(node, xLR)
        self.assertEqual(node.L, xL)
        self.assertEqual(node.R, x)

    def test_balance_right(self):
        x = Node(10, Operation(1, "A"))
        xR = Node(15, Operation(1, "B"))
        xRR = Node(20, Operation(1, "C"))

        x.R = xR
        xR.R = xRR

        Update(xR)
        Update(x)

        node = Balance(x)
        self.assertEqual(node, xR)
        self.assertEqual(node.L, x)
        self.assertEqual(node.R, xRR)

    def test_balance_right_left(self):
        x = Node(10, Operation(1, "A"))
        xR = Node(15, Operation(1, "B"))
        xRL = Node(12, Operation(-1))

        x.R = xR
        xR.L = xRL

        Update(xR)
        Update(x)

        node = Balance(x)
        self.assertEqual(node, xRL)
        self.assertEqual(node.L, x)
        self.assertEqual(node.R, xR)
