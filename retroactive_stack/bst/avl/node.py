from math import inf

from retroactive_stack.operation import Operation


class Node:
    def __init__(self, key=None, operation=None):
        if type(key) is not int:
            raise TypeError("key is not a int")

        if type(operation) is not Operation:
            raise TypeError("operation is not a operation")

        self.key: int = key
        self.min_key: int = key
        self.operation: Operation = operation
        self.L: Node = None
        self.R: Node = None
        self.sum: int = operation.type
        self.max: int = max(0, operation.type)


def Max(node: Node) -> int:
    if node is None:
        return 0

    if not isinstance(node, Node):
        raise TypeError("node is not a Node")

    return node.max


def Type(node: Node) -> int:
    if not isinstance(node, Node):
        raise TypeError("node is not a Node")

    return node.operation.type


def Sum(node: Node) -> int:
    if node is None:
        return 0

    if not isinstance(node, Node):
        raise TypeError("node is not a Node")

    return node.sum


def MinKey(node: Node) -> int:
    if node is None:
        return inf

    if not isinstance(node, Node):
        raise TypeError("node is not a Node")

    return node.min_key


def Update(node: Node):
    if type(node) is not Node:
        raise TypeError("node is not a Node")

    node.min_key = min(
        MinKey(node.L),
        min(
            node.key,
            MinKey(node.R),
        ),
    )

    node.sum = Sum(node.L) + Sum(node.R) + node.operation.type

    node.max = 0
    node.max = max(node.max, Max(node.L))
    node.max = max(node.max, Sum(node.L) + Type(node) + Max(node.R))
    node.max = max(node.max, Sum(node.L) + Type(node))
