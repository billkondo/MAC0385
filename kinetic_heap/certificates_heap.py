from math import inf
from typing import Dict, List

from .certificate import Certificate


class CertificatesHeap:
    """
    Certificates min-heap.
    """

    def __init__(self):
        self.heap: List[Certificate] = []
        self.map_id_to_heap_index: Dict[int, int] = {}

    def insert(self, certificate: Certificate):
        if self.map_id_to_heap_index.get(certificate.id) is not None:
            raise ValueError(
                "cannot insert certificate with repeated"
                + f"id equals {certificate.id}"
            )

        self.heap.append(certificate)
        self.__update_map__(len(self.heap) - 1)
        self.__up_heapify__(len(self.heap) - 1)

    def min(self) -> Certificate:
        return self.heap[0]

    def delete(self, id: int):
        deleted_index = self.map_id_to_heap_index[id]
        self.__delete__(deleted_index)

    def delete_min(self) -> Certificate:
        min_certificate = self.min()
        self.__delete__(0)
        return min_certificate

    def empty(self) -> bool:
        return len(self.heap) == 0

    def update(self, certificate: Certificate):
        id = certificate.id

        if self.map_id_to_heap_index.get(id) is None:
            raise ValueError(f"there is not certificate with id equals {id}")

        updated_index = self.map_id_to_heap_index[id]

        if self.heap[updated_index] == certificate:
            return

        decreased = certificate < self.heap[updated_index]
        self.heap[updated_index] = certificate
        self.__up_heapify__(
            updated_index
        ) if decreased else self.__down_heapify__(updated_index)

    def __delete__(self, deleted_index: int):
        deleted_certificate = self.heap[deleted_index]
        last_index = len(self.heap) - 1
        self.__swap__(deleted_index, last_index)
        self.heap.pop()
        self.map_id_to_heap_index.pop(deleted_certificate.id)
        self.__down_heapify__(deleted_index)

    def __update_map__(self, index: int):
        certificate = self.heap[index]
        self.map_id_to_heap_index[certificate.id] = index

    def __swap__(self, index_1: int, index_2: int):
        self.heap[index_1], self.heap[index_2] = (
            self.heap[index_2],
            self.heap[index_1],
        )

        self.__update_map__(index_1)
        self.__update_map__(index_2)

    def __up_heapify__(self, index: int):
        if index == 0:
            return

        parent_index = index // 2
        if self.heap[parent_index] <= self.heap[index]:
            return

        self.__swap__(parent_index, index)
        self.__up_heapify__(parent_index)

    def __down_heapify__(self, index: int):
        if index >= len(self.heap):
            return

        left_child = index * 2 + 1
        right_child = left_child + 1

        left_certificate = self.__get__(left_child)
        right_certificate = self.__get__(right_child)
        min_certificate = min(left_certificate, right_certificate)

        if min_certificate >= self.heap[index]:
            return

        if min_certificate is left_certificate:
            self.__swap__(left_child, index)
            return self.__down_heapify__(left_child)

        self.__swap__(right_child, index)
        return self.__down_heapify__(right_child)

    def __get__(self, index: int) -> Certificate:
        if index >= len(self.heap):
            return Certificate(inf, inf)

        return self.heap[index]
