from math import inf
from typing import List

from kinetic_heap import Certificate


class CertificatesHeap:
    def __init__(self):
        self.heap: List[Certificate] = []

    def insert(self, certificate: Certificate):
        self.heap.append(certificate)
        self.__insert__(len(self.heap) - 1)

    def delete(self, index: int):
        last_index = len(self.heap) - 1
        self.__swap__(0, last_index)
        self.heap.pop()
        self.__delete__(0)

    def min(self) -> Certificate:
        return self.heap[0]

    def delete_min(self) -> Certificate:
        min_certificate = self.min()
        self.delete(0)
        return min_certificate

    def empty(self) -> bool:
        return len(self.heap) == 0

    def __swap__(self, index_1: int, index_2: int):
        self.heap[index_1], self.heap[index_2] = (
            self.heap[index_2],
            self.heap[index_1],
        )

    def __insert__(self, index: int):
        if index == 0:
            return

        parent_index = index // 2
        if self.heap[parent_index] <= self.heap[index]:
            return

        self.__swap__(parent_index, index)
        self.__insert__(parent_index)

    def __delete__(self, index: int):
        if index >= len(self.heap):
            return

        left_child = index * 2 + 1
        right_child = left_child + 1

        if (
            min(self.__get__(left_child), self.__get__(right_child))
            >= self.heap[index]
        ):
            return

        if self.__get__(left_child) < self.__get__(right_child):
            self.__swap__(left_child, index)
            return self.__delete__(left_child)

        self.__swap__(right_child, index)
        return self.__delete__(right_child)

    def __get__(self, index: int) -> Certificate:
        if index >= len(self.heap):
            return Certificate(inf, inf)

        return self.heap[index]
