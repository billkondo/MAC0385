from typing import List

from retroactive_heap.current_heap.current_heap import CurrentHeap
from retroactive_heap.current_heap.node import Node


class SimpleCurrentHeap(CurrentHeap):
    def __init__(self):
        self.nodes: List[Node] = []

    def insert(self, key: int, time: int):
        for node in self.nodes:
            if node.key == key:
                raise ValueError("repeated key")

        self.nodes.append(Node(key, time))
        self.nodes.sort(key=lambda node: node.time)

    def delete(self, key: int):
        self.nodes = [node for node in self.nodes if node.key != key]

    def min(self, time: int) -> Node:
        min_node: Node = None

        for node in self.nodes:
            if node.time > time:
                continue

            if min_node is None or min_node.key > node.key:
                min_node = node

        return min_node

    def print(self) -> str:
        heap = ""

        for node in self.nodes:
            if len(heap) != 0:
                heap += " "

            heap += str(node.key)

        return heap
