from abc import ABC, abstractmethod

from retroactive_heap.current_heap.node import Node


class CurrentHeap(ABC):
    @abstractmethod
    def insert(self, key: int, time: int):
        pass

    @abstractmethod
    def delete(self, key: int):
        pass

    @abstractmethod
    def min(self, time: int) -> Node:
        pass

    @abstractmethod
    def print(self) -> str:
        pass
