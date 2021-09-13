from typing import Any

from retroactive_stack.bst.avl.node import Node, Sum, Type, Update
from retroactive_stack.bst.bst import BST
from retroactive_stack.operation import Operation


class AVL(BST):
    def __init__(self):
        self.root: Node = None

    def insert(self, key: int, operation: Operation):
        self.root = Insert(self.root, key, operation)

    def delete(self, key: int):
        pass

    def kth(self, key: int, k: int) -> Any:
        pass

    def print(self, key: int) -> str:
        pass

    def size(self, key: int) -> int:
        return Size(self.root, key)


def Insert(node: Node, key: int, operation: Operation) -> Node:
    if node is None:
        return Node(key=key, operation=operation)

    if key <= node.key:
        node.L = Insert(node.L, key, operation)
    else:
        node.R = Insert(node.R, key, operation)

    Update(node)
    return node


def Size(node: Node, key: int) -> int:
    if node is None:
        return 0

    if node.key <= key:
        return Sum(node.L) + Type(node) + Size(node.R, key)

    return Size(node.L, key)
