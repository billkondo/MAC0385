from typing import List, Union


class Node:
    def __init__(self, key: int):
        self.key = key
        self.L: Node = None
        self.R: Node = None
        self.parent: Node = None

    @property
    def is_left_child(self) -> bool:
        return self.parent is not None and self.parent.L is self

    @property
    def is_right_child(self) -> bool:
        return self.parent is not None and self.parent.R is self


class SplayTree:
    def __init__(self):
        self.__root__: Node = None

    def insert(self, key: int):
        node = Node(key)
        self.__root__ = self.__insert__(self.__root__, node)
        self.__splay__(node)

    def __insert__(self, root: Node, node: Node):
        if root is None:
            return node

        if node.key < root.key:
            root.L = self.__insert__(root.L, node)
        else:
            root.R = self.__insert__(root.R, node)

        if root.L is node or root.R is node:
            node.parent = root

        return root

    def search(self, key: int, splay=False) -> bool:
        node = self.__search__(self.__root__, key)
        return True if node is not None else False

    def __search__(self, root: Node, key: int) -> Union[Node, None]:
        if root is None:
            return None

        if root.key == key:
            return root

        if key < root.key:
            return self.__search__(root.L, key)

        return self.__search__(root.R, key)

    def min(self) -> Union[int, None]:
        min_node = self.__min__(self.__root__)
        return min_node.key if min_node is not None else None

    def __min__(self, root: Node) -> Union[Node, None]:
        if root is None:
            return None

        if root.L is None:
            return root

        return self.__min__(root.L)

    def delete(self, key: int):
        deleted_node = self.__search__(self.__root__, key)

        if deleted_node is None:
            raise RuntimeError(f"key {key} is not in splay tree")

        self.__splay__(deleted_node)

        if deleted_node.L is not None:
            deleted_node.L.parent = None

        if deleted_node.R is not None:
            deleted_node.R.parent = None

        self.__root__ = self.__join__(deleted_node.L, deleted_node.R)

    def __join__(self, S: Node, T: Node) -> Node:
        if S is None:
            return T

        if T is None:
            return S

        max_node = self.__max__(S)
        self.__splay__(max_node)
        assert max_node.R is None

        max_node.R = T
        T.parent = max_node

        return max_node

    def __max__(self, root: Node) -> Union[Node, None]:
        if root is None:
            return None

        if root.R is None:
            return root

        return self.__max__(root.R)

    def __splay__(self, root: Node):
        while root.parent is not None:
            grandparent = root.parent.parent
            parent = root.parent

            if grandparent is None:
                self.__rotate_right__(
                    root
                ) if root.is_left_child else self.__rotate_left__(root)
                continue

            if parent.is_left_child and root.is_left_child:
                self.__rotate_right__(parent)
                self.__rotate_right__(root)
                continue

            if parent.is_right_child and root.is_right_child:
                self.__rotate_left__(parent)
                self.__rotate_left__(root)
                continue

            if parent.is_left_child and root.is_right_child:
                self.__rotate_left__(root)
                self.__rotate_right__(root)
                continue

            self.__rotate_right__(root)
            self.__rotate_left__(root)

    def __rotate_right__(self, node: Node):
        right_child = node.R
        parent = node.parent
        is_parent_left_child = parent.is_left_child
        grandparent = node.parent.parent

        node.R = parent
        parent.parent = node

        parent.L = right_child
        if right_child is not None:
            right_child.parent = parent

        if grandparent is not None:
            if is_parent_left_child:
                grandparent.L = node
            else:
                grandparent.R = node
            node.parent = grandparent
        else:
            node.parent = None

        if self.__root__ is parent:
            self.__root__ = node

    def __rotate_left__(self, node: Node):
        left_child = node.L
        parent = node.parent
        is_parent_left_child = parent.is_left_child
        grandparent = node.parent.parent

        node.L = parent
        parent.parent = node

        parent.R = left_child
        if left_child is not None:
            left_child.parent = parent

        if grandparent is not None:
            if is_parent_left_child:
                grandparent.L = node
            else:
                grandparent.R = node
            node.parent = grandparent
        else:
            node.parent = None

        if self.__root__ is parent:
            self.__root__ = node

    def print(self) -> List[str]:
        return self.__print__(self.__root__)

    def __print__(self, root: Node) -> List[str]:
        keys = []
        self.__pre_order__(root, keys)
        return keys

    def __pre_order__(self, root: Node, keys: List[str]):
        if root is None:
            return

        keys.append(str(root.key))

        self.__pre_order__(root.L, keys)
        self.__pre_order__(root.R, keys)
