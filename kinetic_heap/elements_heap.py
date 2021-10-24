from math import inf
from typing import Dict, List

from kinetic_heap.certificate import Certificate

from .certificates_heap import CertificatesHeap
from .element import Element
from .utils import create_certificate


class ElementsHeap:
    def __init__(self):
        self.heap: List[Element] = []
        self.certificates_heap: CertificatesHeap = CertificatesHeap()
        self.current_time: float = 0
        self.map_id_to_heap_index: Dict[int, int] = {}

    def insert(self, element: Element):
        self.heap.append(element)

        index = len(self.heap) - 1
        self.__add_parent_certificate__(index)
        self.__update_map__(index)
        self.__up_heapify__(index)

    def max(self) -> Element:
        return self.heap[0]

    def delete(self, id: int):
        deleted_index = self.map_id_to_heap_index[id]
        self.__delete__(deleted_index)

    def delete_max(self):
        self.__delete__(0)

    def update(self, id: int, speed: float):
        if self.map_id_to_heap_index.get(id) is None:
            raise ValueError(f"there is not element with id equals {id}")

        updated_index = self.map_id_to_heap_index[id]
        old_speed = self.heap[updated_index].speed
        self.__update_speed_from_element__(id, speed)
        self.__update_certificates__(updated_index)

        if old_speed < speed:
            self.__up_heapify__(updated_index)
        else:
            self.__down_heapify__(updated_index)

    def advance(self, current_time: float):
        if current_time < self.current_time:
            raise ValueError("cannot decrease current_time")

        while (
            not self.certificates_heap.empty()
            and self.certificates_heap.min().expiration_time < current_time
        ):
            self.__expired__(self.certificates_heap.min())

        self.current_time = current_time

    def __expired__(self, certificate: Certificate):
        expired_index = self.map_id_to_heap_index[certificate.id]
        parent_index = expired_index // 2
        self.__swap__(expired_index, parent_index)
        self.current_time = certificate.expiration_time

    def __delete__(self, deleted_index: int):
        deleted_element = self.heap[deleted_index]
        last_index = len(self.heap) - 1
        self.__swap__(deleted_index, last_index)
        self.heap.pop()
        self.map_id_to_heap_index.pop(deleted_element.id)
        self.certificates_heap.delete(deleted_element.id)
        self.__down_heapify__(deleted_index)

    def __update_map__(self, index: int):
        element = self.heap[index]
        self.map_id_to_heap_index[element.id] = index

    def __swap__(self, index_1: int, index_2: int):
        self.heap[index_1], self.heap[index_2] = (
            self.heap[index_2],
            self.heap[index_1],
        )

        self.__update_map__(index_1)
        self.__update_map__(index_2)

        self.__update_certificates__(index_1)
        self.__update_certificates__(index_2)

    def __update_certificates__(self, index: int):
        left_child = index * 2 + 1
        right_child = left_child + 1
        sibling = self.__sibling__(index)

        self.__update_certificate_with_parent__(index)

        if left_child < len(self.heap):
            self.__update_certificate_with_parent__(left_child)

        if right_child < len(self.heap):
            self.__update_certificate_with_parent__(right_child)

        if sibling is not None:
            self.__update_certificate_with_parent__(sibling)

    def __sibling__(self, index: int):
        if index == 0:
            return None

        parent_index = index // 2
        parent_left_child = parent_index * 2 + 1
        parent_right_child = parent_left_child + 1

        sibling = (
            parent_left_child
            if index != parent_left_child
            else parent_right_child
        )

        return sibling if sibling < len(self.heap) else None

    def __update_certificate_with_parent__(self, index: int):
        if index == 0:
            return self.certificates_heap.update(
                Certificate(
                    inf,
                    self.heap[0].id,
                ),
            )

        parent_index = index // 2
        self.certificates_heap.update(
            create_certificate(
                self.heap[index],
                self.heap[parent_index],
            ),
        )

    def __add_parent_certificate__(self, index: int):
        if index == 0:
            return self.certificates_heap.insert(
                Certificate(
                    inf,
                    self.heap[0].id,
                )
            )

        parent_index = index // 2
        self.certificates_heap.insert(
            create_certificate(
                self.heap[index],
                self.heap[parent_index],
            ),
        )

    def __up_heapify__(self, index: int):
        self.__update_certificates__(index)

        if index == 0:
            return

        parent_index = index // 2
        if self.__compare_elements__(
            self.heap[index],
            self.heap[parent_index],
        ):
            return

        self.__swap__(index, parent_index)
        self.__up_heapify__(parent_index)

    def __down_heapify__(self, index: int):
        if index >= len(self.heap):
            return

        self.__update_certificates__(index)

        left_child = index * 2 + 1
        right_child = left_child + 1

        left_element = self.__element_from_index__(left_child)
        right_element = self.__element_from_index__(right_child)
        max_element = self.__max_elements__(left_element, right_element)

        if self.__compare_elements__(
            max_element,
            self.heap[index],
        ):
            return

        if max_element is left_element:
            self.__swap__(left_child, index)
            return self.__down_heapify__(left_child)

        self.__swap__(right_child, index)
        return self.__down_heapify__(right_child)

    def __element_from_index__(self, index: int) -> Element:
        if index >= len(self.heap):
            return Element(-inf, -inf, -inf)

        return self.heap[index]

    def __compare_elements__(self, first: Element, second: Element) -> bool:
        x1 = first.x0 + first.speed * self.current_time
        x2 = second.x0 + second.speed * self.current_time

        return (x1, first.speed, first.id) <= (x2, second.speed, second.id)

    def __max_elements__(self, first: Element, second: Element) -> Element:
        return second if self.__compare_elements__(first, second) else first

    def __update_speed_from_element__(self, id: int, speed: float):
        updated_index = self.map_id_to_heap_index[id]
        updated_element = self.heap[updated_index]

        x = updated_element.x0 + updated_element.speed * self.current_time
        x0 = x - speed * self.current_time

        self.heap[updated_index] = Element(updated_element.id, x0, speed)
