from math import inf
from typing import Dict, List

from avl.avl_node import AVLNode
from avl.interface import Delete, Find, Insert
from retroactive_heap.current_heap.current_heap import CurrentHeap
from retroactive_heap.current_heap.node import Node


class AVLCurrentHeap(CurrentHeap):
    def __init__(self):
        self.root: CurrentHeapAVLNode = None
        self.key_insert_time: Dict[int, int] = {}

    def insert(self, key: int, time: int):
        self.key_insert_time[key] = time
        self.root = Insert(
            self.root,
            CurrentHeapAVLNode(
                key=key,
                time=time,
            ),
        )

    def delete(self, key: int):
        self.root = Delete(
            self.root,
            self.key_insert_time[key],
        )
        self.key_insert_time.pop(key)

    def min(self, time: int) -> Node:
        min_key = Min(self.root, time)
        min_node = Find(self.root, self.key_insert_time[min_key])

        return None if min_node is None else min_node.node

    def print(self) -> str:
        return Print(self.root)


class CurrentHeapAVLNode(AVLNode):
    def __init__(self, key=None, time=None):
        super().__init__(key=time)

        self.node: Node = Node(key=key, time=time)
        self.min_time: int = time
        self.max_time: int = time
        self.min_node_key: int = key

    def update(self):
        super().update()
        self.min_time = self.min_key
        self.max_time = max(
            MaxTime(self.L), max(self.max_time, MaxTime(self.R))
        )
        self.min_node_key = min(
            MinNodeKey(self.L), min(self.node.key, MinNodeKey(self.R))
        )

    @property
    def time(self):
        return self.node.time


def MinNodeKey(node: CurrentHeapAVLNode) -> int:
    if node is None:
        return inf

    if not isinstance(node, CurrentHeapAVLNode):
        raise TypeError("node is not a CurrentHeapAVLNode")

    return node.min_node_key


def MaxTime(node: CurrentHeapAVLNode) -> int:
    if node is None:
        return 0

    if not isinstance(node, CurrentHeapAVLNode):
        raise TypeError("node is not a CurrentHeapAVLNode")

    return node.max_time


def Min(node: CurrentHeapAVLNode, time: int) -> int:
    if node is None:
        return inf

    if not isinstance(node, CurrentHeapAVLNode):
        raise TypeError("node is not a CurrentHeapAVLNode")

    if time < node.min_time:
        return inf

    if MaxTime(node) <= time:
        return MinNodeKey(node)

    return min(Min(node.L, time), Min(node.R, time))


def Print(node: CurrentHeapAVLNode) -> str:
    if node is None:
        return ""

    if not isinstance(node, CurrentHeapAVLNode):
        raise TypeError("node is not a CurrentHeapAVLNode")

    def _Print(node: CurrentHeapAVLNode, list: List[str]):
        if node is None:
            return

        _Print(node.L, list)
        list.append(str(node.node.key))
        _Print(node.R, list)

    node_list = []
    _Print(node, node_list)

    return " ".join(node_list)
