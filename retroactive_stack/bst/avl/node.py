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


def Sum(node: Node) -> int:
    if node is None:
        return 0

    if not isinstance(node, Node):
        raise TypeError("node is not a Node")

    return node.sum


def Update(node: Node):
    if type(node) is not Node:
        raise TypeError("node is not a Node")

    node.sum = Sum(node.L) + Sum(node.R)
