from typing import Any

from persistent_bst.bst import BST
from persistent_bst.node.interface import (
    CopyNode,
    DeleteNode,
    InsertNode,
    MinNode,
    PrintNode,
    SearchNode,
)


def NewBST() -> BST:
    return BST()


def Empty(b: BST) -> bool:
    if b is None:
        raise ValueError("b is None")

    if type(b) != BST:
        raise TypeError("b is not a BST")

    return b.root is None


def CopyBST(b: BST) -> BST:
    if b is None:
        raise ValueError("b is None")

    root_copy = CopyNode(b.root)
    return BST(root_copy)


def Insert(b: BST, value) -> BST:
    if b is None:
        raise ValueError("b is None")

    if type(b) != BST:
        raise TypeError("b is not a BST")

    return BST(InsertNode(b.root, value))


def Search(b: BST, value) -> bool:
    if b is None:
        raise ValueError("b is None")

    if type(b) != BST:
        raise TypeError("b is not a BST")

    return SearchNode(b.root, value)


def Delete(b: BST, value) -> BST:
    if b is None:
        raise ValueError("b is None")

    if type(b) != BST:
        raise TypeError("b is not a BST")

    if not SearchNode(b.root, value):
        raise RuntimeError("value is not in b")

    return BST(DeleteNode(b.root, value))


def Min(b: BST) -> Any:
    if b is None:
        raise ValueError("b is None")

    if type(b) != BST:
        raise TypeError("b is not a BST")

    if Empty(b):
        raise ValueError("b is empty")

    return MinNode(b.root).value


def Print(b: BST) -> str:
    return PrintNode(b.root)
