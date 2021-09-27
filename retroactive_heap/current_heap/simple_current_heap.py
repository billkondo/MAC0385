import math
from typing import List

from retroactive_heap.current_heap.current_heap import CurrentHeap, Node


class SimpleCurrentHeap(CurrentHeap):
    def __init__(self):
        self.nodes: List[Node] = []

    def insert(self, key: int, time: int):
        self.nodes.append(Node(key, time))
        self.nodes.sort(key=lambda node: node.key)

    def delete(self, key: int):
        self.nodes = [node for node in self.nodes if node.key != key]

    def min(self, time: int) -> int:
        min_key = math.inf

        for node in self.nodes:
            if node.time <= time:
                min_key = min(min_key, node.key)

        return min_key

    def print(self) -> str:
        heap = ""

        for node in self.nodes:
            if len(heap) != 0:
                heap += " "

            heap += str(node.key)

        return heap
