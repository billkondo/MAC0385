from abc import ABC, abstractmethod

from retroactive_heap.operations_bst.operation import Operation


class BST(ABC):
    @abstractmethod
    def insert(self, time: int, type: int, key: int = None):
        pass

    @abstractmethod
    def delete(self, time: int):
        pass

    @abstractmethod
    def previous_bridge_time(self, time: int) -> int:
        pass

    @abstractmethod
    def next_bridge_time(self, time: int) -> int:
        pass

    @abstractmethod
    def find(self, time: int) -> Operation:
        pass

    @abstractmethod
    def operation_with_greatest_key_after_time(self, time: int) -> Operation:
        pass
