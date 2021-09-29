from abc import ABC, abstractclassmethod, abstractmethod

from retroactive_heap.operations_bst.operation import Operation


class BST(ABC):
    @abstractmethod
    def insert(self, time: int, type: int, key: int = None):
        pass

    @abstractclassmethod
    def delete(self, time: int):
        pass

    @abstractclassmethod
    def previous_bridge_time(self, time: int) -> int:
        pass

    @abstractclassmethod
    def next_bridge_time(self, time: int) -> int:
        pass

    @abstractclassmethod
    def max(self, time: int) -> Operation:
        pass
