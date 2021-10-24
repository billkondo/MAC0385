from typing import List

from .elements_heap import ElementsHeap


class KineticHeap:
    """
    Kinetic Heap

    The implementation of the kinetic heap operations is in ``ElementsHeap``.
    """

    def __init__(
        self,
        id_list: List[int] = [],
        x0_list: List[float] = [],
        speed_list: List[float] = [],
        n: int = 0,
    ):
        if n is None or type(n) is not int:
            raise TypeError("n is not a int")

        if len(id_list) != n:
            raise ValueError("id_list length is not n")

        if len(x0_list) != n:
            raise ValueError("x0_list length is not n")

        if len(speed_list) != n:
            raise ValueError("speed_list length is not n")

        self.elements_heap = ElementsHeap()
        for i in range(0, n):
            self.insert(id_list[i], x0_list[i], speed_list[i])

    def advance(self, current_time: int):
        self.elements_heap.advance(current_time)

    def change(self, id: int, speed: float):
        self.elements_heap.update(id, speed)

    def insert(self, id: int, x_now: float, speed: float):
        self.elements_heap.insert(
            id,
            x_now,
            speed,
        )

    def max(self) -> int:
        return self.elements_heap.max().id

    def delete_max(self) -> float:
        self.elements_heap.delete_max()

    def delete(self, id: int):
        self.elements_heap.delete(id)

    def print() -> List[str]:
        pass
