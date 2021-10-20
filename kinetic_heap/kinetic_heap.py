from typing import List


class KineticHeap:
    def __init__(
        self,
        id_list: List[str] = [],
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

        self.n: int = n
        self.id_list: List[str] = id_list
        self.x0_list: List[float] = x0_list
        self.speed_list: List[float] = speed_list
        self.t = 0

    def advance(self, t: int):
        pass

    def change(self, id: str, speed: float):
        pass

    def insert(self, id: str, xnow: float, speed: float):
        pass

    def max(self) -> str:
        pass

    def delete_max() -> float:
        pass

    def delete(id: str):
        pass

    def print() -> List[str]:
        pass
