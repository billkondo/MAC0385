import unittest

from retroactive_heap.operations_bst.operation import Operation


class TestOperation(unittest.TestCase):
    def test_operation(self):
        self.assertRaises(TypeError, lambda: Operation(key="123"))
        self.assertRaises(TypeError, lambda: Operation(type="2"))
        self.assertRaises(TypeError, lambda: Operation(type=10))
        self.assertRaises(TypeError, lambda: Operation(type=-10))

        operation = Operation(key=10, type=0)
        self.assertEqual(operation.key, 10)
        self.assertEqual(operation.type, 0)
