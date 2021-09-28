import unittest

from retroactive_heap.operations_bst.operation import Operation


class TestOperation(unittest.TestCase):
    def test_operation(self):
        self.assertRaises(TypeError, lambda: Operation(time="20"))
        self.assertRaises(
            TypeError,
            lambda: Operation(
                time=1,
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
        self.assertRaises(
            TypeError,
            lambda: Operation(
                time=1,
                type=0,
                key="123",
            ),
        )

        operation = Operation(
            time=15,
            type=0,
            key=10,
        )
        self.assertEqual(operation.time, 15)
        self.assertEqual(operation.key, 10)
        self.assertEqual(operation.type, 0)

        operation_empty_key = Operation(
            time=12,
            type=-1,
        )
        self.assertEqual(operation_empty_key.time, 12)
        self.assertEqual(operation_empty_key.type, -1)
