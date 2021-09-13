from typing import Any, List

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
        top = self.size(key)
        node = Find(self.root, key, 0, top - k + 1)
        return None if node is None else node.operation.value

    def print(self, key: int) -> str:
        stack = []
        Collect(self.root, key, stack)
        stack.reverse()
        return " ".join(stack)

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


def Find(node: Node, key: int, left_sum: int, top: int) -> Node:
    if node is None:
        return None

    if node.max < top or key < node.min_key:
        return None

    candidate = Find(node.R, key, left_sum + Sum(node.L) + Type(node), top)
    if candidate is not None:
        return candidate

    if Type(node) == 1 and left_sum + Sum(node.L) + Type(node) == top:
        return node

    return Find(node.L, key, left_sum, top)


def Collect(node: Node, key: int, stack: List[str]):
    if node is None:
        return

    if key < node.min_key:
        return

    Collect(node.L, key, stack)

    if node.key <= key:
        if Type(node) == 1:
            stack.append(str(node.operation.value))
        else:
            stack.pop()

    Collect(node.R, key, stack)
