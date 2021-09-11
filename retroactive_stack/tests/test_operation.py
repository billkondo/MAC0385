import unittest

from retroactive_stack.operation import Operation

class OperationTest(unittest.TestCase):
  def test_constructor(self):
    self.assertRaises(ValueError, lambda: Operation(type=10))
    self.assertRaises(ValueError, lambda: Operation())
    self.assertRaises(ValueError, lambda: Operation(type=-1, value="A"))
    self.assertRaises(ValueError, lambda: Operation(type=1))

    operation = Operation(type=1, value="A")
    self.assertEqual(operation.type, 1)
    self.assertEqual(operation.value, "A")