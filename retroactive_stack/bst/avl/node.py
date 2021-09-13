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
        self.sum: int = operation.type
        self.max: int = max(0, operation.type)
        self.prefix_max = max(0, operation.type)


def Max(node: Node) -> int:
    if node is None:
        return 0

    if not isinstance(node, Node):
        raise TypeError("node is not a Node")

    return node.max


def PrefixMax(node: Node) -> int:
    if node is None:
        return 0

    if not isinstance(node, Node):
        raise TypeError("node is not a Node")

    return node.prefix_max


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


def Update(node: Node):
    if type(node) is not Node:
        raise TypeError("node is not a Node")

    node.sum = Sum(node.L) + Sum(node.R) + node.operation.type

    node.prefix_max = 0
    node.prefix_max = max(node.prefix_max, PrefixMax(node.L))
    node.prefix_max = max(node.prefix_max, PrefixMax(node.R))
    node.prefix_max = max(
        node.prefix_max,
        Sum(node.L) + Type(node) + PrefixMax(node.R),
    )

    node.max = 0
    node.max = max(node.max, Max(node.L))
    node.max = max(node.max, Max(node.R))
    node.max = max(node.max, node.prefix_max)
