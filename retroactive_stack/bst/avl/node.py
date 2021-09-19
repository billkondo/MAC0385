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
        self.height: int = 0
        self.balance: int = 0


def Height(node: Node) -> int:
    if node is None:
        return -1

    return node.height


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

    node.sum = Sum(node.L) + Sum(node.R) + Type(node)

    node.max = 0
    node.max = max(node.max, Max(node.L))
    node.max = max(node.max, Sum(node.L) + Type(node) + Max(node.R))
    node.max = max(node.max, Sum(node.L) + Type(node))

    node.height = max(Height(node.L), Height(node.R)) + 1
    node.balance = Height(node.R) - Height(node.L)


def RotateRight(node: Node) -> Node:
    #          x             y
    #        / |           / |
    #       y  T3   =>   T1  x
    #     / |              / |
    #   T1  T2           T2  T3

    if not isinstance(node, Node):
        raise TypeError("node is not a node")

    if node.L is None:
        return node

    x = node
    y = node.L
    t2 = y.R

    y.R = x
    x.L = t2

    Update(x)
    Update(y)

    return y


def RotateLeft(node: Node) -> Node:
    #          y               x
    #        / |             / |
    #      T1  x   =>       y  T3
    #        / |          / |
    #      T2  T3       T1  T2

    if not isinstance(node, Node):
        raise TypeError("node is not a node")

    if node.R is None:
        return node

    y = node
    x = node.R
    t2 = x.L

    y.R = t2
    x.L = y

    Update(y)
    Update(x)

    return x


def Balance(node: Node) -> Node:
    if not isinstance(node, Node):
        raise TypeError("node is not a node")

    if node.balance <= -2:
        if node.L is not None and node.L.balance <= 0:
            return RotateRight(node)

        node.L = RotateLeft(node.L)
        return RotateRight(node)

    if node.balance >= 2:
        if node.R is not None and node.R.balance >= 0:
            return RotateLeft(node)

        node.R = RotateRight(node.R)
        return RotateLeft(node)

    return node
