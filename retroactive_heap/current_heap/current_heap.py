from abc import ABC


class CurrentHeap(ABC):
    def insert(self, key: int, time: int):
        pass

    def delete(self, key: int):
        pass

    def min(self, key: int, time: int) -> int:
        pass

    def print(self) -> str:
        pass


class Node:
    def __init__(self, key=None, time=None):
        if not isinstance(key, int):
            raise ValueError('key is not a int')

        if not isinstance(time, int):
            raise ValueError('time is not a int')

        self.key: int = key
        self.time: int = time
