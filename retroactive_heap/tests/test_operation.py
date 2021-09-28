import unittest

from retroactive_heap.operations_bst.operation import Operation


class TestOperation(unittest.TestCase):
    def test_operation(self):
        self.assertRaises(TypeError, lambda: Operation(time="20"))
        self.assertRaises(TypeError, lambda: Operation(time=1, key="123"))
        self.assertRaises(
            TypeError,
            lambda: Operation(
                time=1,
                key=10,
                type="2",
            ),
        )
        self.assertRaises(
            ValueError,
            lambda: Operation(
                time=1,
                key=10,
                type=10,
            ),
        )
        self.assertRaises(
            ValueError,
            lambda: Operation(
                time=1,
                key=10,
                type=-10,
            ),
        )

        operation = Operation(15, 10, 0)
        self.assertEqual(operation.time, 15)
        self.assertEqual(operation.key, 10)
        self.assertEqual(operation.type, 0)
