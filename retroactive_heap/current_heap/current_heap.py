from abc import ABC, abstractmethod


class CurrentHeap(ABC):
    @abstractmethod
    def insert(self, key: int, time: int):
        pass

    def delete(self, key: int):
        pass

    @abstractmethod
    def min(self, time: int) -> int:
        pass

    @abstractmethod
    def print(self) -> str:
        pass


class Node:
    def __init__(self, key=None, time=None):
        if not isinstance(key, int):
            raise TypeError("key is not a int")

        if not isinstance(time, int):
            raise TypeError("time is not a int")

        self.key: int = key
        self.time: int = time
