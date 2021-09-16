from persistent_deque.deque import Deque
from persistent_deque.node.interface import (
    AddLeaf,
    Depth,
    LevelAncestor,
    LowestCommonAncestor,
)
from persistent_deque.node.node import Node


def deque_validator(function):
    def wrapper(*args):
        deque = args[0]
        if deque is None or type(deque) != Deque:
            raise TypeError("deque is not a Deque")

        return function(*args)

    return wrapper


def NewDeque() -> Deque:
    return Deque(None, None)


@deque_validator
def Front(deque: Deque):
    return deque.first.value


@deque_validator
def Back(deque: Deque):
    return deque.last.value


@deque_validator
def PushFront(deque: Deque, value: int) -> Deque:
    if deque.first is None:
        root = AddLeaf(value, None)
        return Deque(root, root)
    else:
        return Deque(AddLeaf(value, deque.first), deque.last)


@deque_validator
def Swap(deque: Deque) -> Deque:
    return Deque(deque.last, deque.first)


@deque_validator
def PushBack(deque: Deque, value: int) -> Deque:
    return Swap(PushFront(Swap(deque), value))


@deque_validator
def _Kth(deque: Deque, k: int) -> Node:
    if k is None or type(k) != int:
        raise TypeError("k is not an integer")

    if k < 0:
        raise ValueError("k is less than zero")

    u = deque.first
    v = deque.last

    mid = LowestCommonAncestor(u, v)

    path_length = Depth(u) + Depth(v) - 2 * Depth(mid)
    if k > path_length:
        raise ValueError("k is greater than path length")

    first_half_length = Depth(u) - Depth(mid)
    is_in_first_half = k <= first_half_length

    if is_in_first_half:
        return LevelAncestor(k, u)

    second_half_length = Depth(v) - Depth(mid)
    return LevelAncestor(second_half_length - (k - first_half_length), v)


@deque_validator
def Kth(deque: Deque, k: int) -> int:
    kth = _Kth(deque, k)
    return kth.value


@deque_validator
def PopFront(deque: Deque) -> Deque:
    if deque.first is None:
        raise ValueError("deque is empty")

    if deque.first == deque.last:
        return NewDeque()

    return Deque(_Kth(deque, 1), deque.last)


@deque_validator
def PopBack(deque: Deque) -> Deque:
    return Swap(PopFront(Swap(deque)))


@deque_validator
def Print(deque: Deque) -> str:
    deque_str = ""

    while deque.first is not None:
        if len(deque_str) != 0:
            deque_str += " "

        deque_str += str(deque.first.value)
        deque = PopFront(deque)

    return deque_str
