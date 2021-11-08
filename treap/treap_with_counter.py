from typing import Union

from .treap import Node, Treap


def with_counter(f):
    def wrapper(*args, **kwargs):
        self = args[0]
        root = args[1] if len(args) > 1 else kwargs["root"]

        if root is not None:
            self.__counter__ += 1

        return f(*args, **kwargs)

    return wrapper


class TreapWithCounter(Treap):
    def __init__(self):
        self.__counter__ = 0
        super().__init__()

    def reset(self):
        self.__counter__ = 0

    @property
    def counter(self):
        return self.__counter__

    @with_counter
    def __insert__(self, root: Node, node: Node) -> Node:
        return super().__insert__(root, node)

    @with_counter
    def __search__(self, root: Node, key: int) -> Union[Node, None]:
        return super().__search__(root, key)
