import unittest

from retroactive_stack.bst.avl.node import Node, Sum
from retroactive_stack.operation import Operation


class NodeTest(unittest.TestCase):
    def test_constructor(self):
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

        operation = Operation(type=1, value="A")
        node = Node(key=10, operation=operation)

        self.assertEqual(node.key, 10)
        self.assertEqual(node.operation, operation)
        self.assertIsNone(node.L)
        self.assertIsNone(node.R)
        self.assertEqual(node.sum, 0)

    def test_sum(self):
        self.assertRaises(TypeError, lambda: Sum('invalid'))

        self.assertEqual(Sum(None), 0)

        node = Node(
            key=10,
            operation=Operation(
                type=1,
                value="A",
            ),
        )
        node.sum = 10
        self.assertEqual(Sum(node), 10)
