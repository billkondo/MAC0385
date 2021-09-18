import unittest
from unittest.mock import Mock

from retroactive_stack.bst.avl.node import Max, Node, Sum, Type, Update
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
        node.L = L

        R = Mock(spec=Node)
        R.sum = -5
        R.max = 8
        R.min_key = 10
        node.R = R

        Update(node)
        self.assertEqual(node.sum, 0)
        self.assertEqual(node.max, 13)
        self.assertEqual(node.min_key, 2)
