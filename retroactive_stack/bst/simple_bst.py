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

    def kth(self, key: int, k: int) -> Any:
        stk = self.stack(key)

        return stk[-k]

    def size(self, key: int) -> int:
        stk = self.stack(key)

        return len(stk)

    def print(self, key: int) -> str:
        stk = self.stack(key)
        stk.reverse()

        stk_str = ""
        for value in stk:
            if len(stk_str) != 0:
                stk_str += " "

            stk_str += str(value)

        return stk_str

    def operations(self):
        return list(map(lambda node: node.operation, self.nodes))

    def stack(self, key: int) -> List[Any]:
        stk = []

        for node in self.nodes:
            if node.key > key:
                break

            if node.operation.type == -1:
                stk.pop()
                continue

            stk.append(node.operation.value)

        return stk
