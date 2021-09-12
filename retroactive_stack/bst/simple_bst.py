from typing import Any, List

from retroactive_stack.bst.bst import BST
from retroactive_stack.operation import Operation


class Node:
    def __init__(self, key=None, operation=None):
        self.key: int = key
        self.operation: Operation = operation


class SimpleBST(BST):
    def __init__(self):
        self.nodes: List[Node] = []

    def insert(self, key: int, operation: Operation):
        self.nodes.append(Node(key=key, operation=operation))
        self.nodes.sort(key=lambda op: op.key)

    def delete(self, key: int):
        self.nodes = [node for node in self.nodes if node.key != key]

    def count_less_than(self, key: int) -> int:
        count = 0

        for node in self.nodes:
            if node.key <= key:
                count += 1

        return count

    def kth(self, key: int, k: int) -> Any:
        stk = []

        for node in self.nodes:
            if node.key > key:
                break

            if node.operation.type == -1:
                stk.pop()
                continue

            stk.append(node.operation.value)

        return stk[-k]

    def operations(self):
        return list(map(lambda node: node.operation, self.nodes))
