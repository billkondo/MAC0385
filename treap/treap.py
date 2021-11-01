from math import inf
from random import random
from typing import List, Union


class Node:
    def __init__(self, key: int):
        self.key = key
        self.priority = random()
        self.L: Node = None
        self.R: Node = None

    @property
    def is_heap(self):
        return self.priority >= max(Priority(self.L), Priority(self.R))


class Treap:
    def __init__(self):
        self.__root__: Node = None

    def insert(self, key: int):
        node = Node(key)
        self.__root__ = self.__insert__(self.__root__, node)

    def __insert__(self, root: Node, node: Node) -> Node:
        if root is None:
            return node

        if node.key < root.key:
            root.L = self.__insert__(root.L, node)
        else:
            root.R = self.__insert__(root.R, node)

        return self.__rotate__(root)

    def delete(self, key: int):
        self.__root__ = self.__delete__(self.__root__, key)

    def __delete__(self, root: Node, key: int) -> Node:
        if root is None:
            raise RuntimeError(f"key {key} is not in the treap")

        if root.key == key:
            if root.R is not None:
                min_node = self.__min__(root.R)
                min_node.R = self.__delete__(root.R, min_node.key)
                min_node.L = root.L

                return self.__push_down__(min_node)

            if root.L is not None:
                return root.L

            return None

        if key < root.key:
            root.L = self.__delete__(root.L, key)
        else:
            root.R = self.__delete__(root.R, key)

        return self.__rotate__(root)

    def __push_down__(self, root: Node):
        if root is None:
            return

        if root.is_heap:
            return root

        root = self.__rotate__(root)
        root.L = self.__push_down__(root.L)
        root.R = self.__push_down__(root.R)

        return root

    def search(self, key: int) -> bool:
        node = self.__search__(self.__root__, key)
        return True if node is not None else False

    def __search__(self, root: Node, key: int) -> Union[Node, None]:
        if root is None:
            return None

        if root.key == key:
            return root

        if key < root.key:
            return self.__search__(root.L, key)

        return self.__search__(root.R, key)

    def min(self) -> int:
        min_node = self.__min__(self.__root__)
        return min_node.key if min_node is not None else None

    def __min__(self, root: Node) -> Union[Node, None]:
        if root is None:
            return None

        if root.L is None:
            return root

        return self.__min__(root.L)

    def print(self) -> List[str]:
        keys = []
        self.__pre_order__(self.__root__, keys)
        return keys

    def __pre_order__(self, root: Node, keys: List[str]):
        if root is None:
            return

        keys.append(str(root.key))

        self.__pre_order__(root.L, keys)
        self.__pre_order__(root.R, keys)

    def __rotate__(self, node: Node) -> Node:
        if node.is_heap:
            return node

        if Priority(node.R) >= Priority(node.L):
            return self.__rotate_left__(node)

        return self.__rotate_right__(node)

    def __rotate_left__(self, root: Node) -> Node:
        new_root = root.R
        root.R = new_root.L
        new_root.L = root
        return new_root

    def __rotate_right__(self, root: Node) -> Node:
        new_root = root.L
        root.L = new_root.R
        new_root.R = root
        return new_root


def Priority(node: Node) -> int:
    return -inf if node is None else node.priority
