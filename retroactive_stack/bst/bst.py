from abc import ABC, abstractmethod
from typing import Any

from retroactive_stack.operation import Operation


class BST(ABC):
    @abstractmethod
    def insert(self, key: int, operation: Operation):
        pass

    @abstractmethod
    def delete(self, key: int):
        pass

    @abstractmethod
    def count_less_than(self, key: int) -> int:
        pass

    @abstractmethod
    def kth(self, key: int, k: int) -> Any:
        pass
