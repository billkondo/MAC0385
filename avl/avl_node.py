from math import inf


class AVLNode:
    def __init__(self, key=None):
        if not isinstance(key, int):
            raise TypeError("key is not a int")

        self.key: int = key
        self.min_key: int = key
        self.max_key: int = key

        self.L: AVLNode = None
        self.R: AVLNode = None

        self.height: int = 0
        self.balance: int = 0

    def update(self):
        self.min_key = min(MinKey(self.L), min(self.key, MinKey(self.R)))
        self.max_key = max(MaxKey(self.L), max(self.key, MaxKey(self.R)))
        self.height = max(Height(self.L), Height(self.R)) + 1
        self.balance = Height(self.R) - Height(self.L)


def MinKey(node: AVLNode) -> int:
    if node is None:
        return inf

    if not isinstance(node, AVLNode):
        raise TypeError("node is not a AVLNode")

    return node.min_key


def MaxKey(node: AVLNode) -> int:
    if node is None:
        return -inf

    if not isinstance(node, AVLNode):
        raise TypeError("node is not a AVLNode")

    return node.max_key


def Height(node: AVLNode) -> int:
    if node is None:
        return -1

    if not isinstance(node, AVLNode):
        raise TypeError("node is not a AVLNode")

    return node.height
