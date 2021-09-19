import unittest
from unittest.mock import Mock

from retroactive_stack.bst.avl.node import (
    Height,
    Max,
    Node,
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
        self.assertEqual(pop_node.max, 0)
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
        self.assertEqual(Max(None), 0)

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
        L.min_key = 2
        L.height = 4
        node.L = L

        R = Mock(spec=Node)
        R.sum = -5
        R.max = 8
        R.min_key = 10
        R.height = 5
        node.R = R

        Update(node)
        self.assertEqual(node.sum, 0)
        self.assertEqual(node.max, 13)
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
        R.min_key = 14
        R.height = 2
        node.R = R

        Update(node)
        self.assertEqual(node.sum, 4)
        self.assertEqual(node.max, 1)
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
        L.min_key = 2
        L.height = 4
        node.L = L

        Update(node)
        self.assertEqual(node.sum, 9)
        self.assertEqual(node.max, 11)
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

        self.assertEqual(x.sum, -1)
        self.assertEqual(x.max, 0)
