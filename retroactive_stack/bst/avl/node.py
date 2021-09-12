from retroactive_stack.operation import Operation


class Node:
    def __init__(self, key=None, operation=None):
        if type(key) is not int:
            raise TypeError("key is not a int")

        if type(operation) is not Operation:
            raise TypeError("operation is not a operation")

        self.key: int = key
        self.operation: Operation = operation
        self.L: Node = None
        self.R: Node = None
        self.sum = 0
