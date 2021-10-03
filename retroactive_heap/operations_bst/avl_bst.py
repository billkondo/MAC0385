from math import inf
from typing import Tuple

from avl.avl_node import AVLNode
from avl.interface import Delete, Find, Insert
from retroactive_heap.operations_bst.bst import BST
from retroactive_heap.operations_bst.operation import Operation


class AVLBST(BST):
    def __init__(self):
        self.root: AVLBSTNode = None

    def insert(self, time: int, type: int, key: int = None):
        self.root = Insert(
            self.root,
            AVLBSTNode(
                Operation(
                    time=time,
                    type=type,
                    key=key,
                )
            ),
        )

    def delete(self, time: int):
        self.root = Delete(self.root, time)

    def find(self, time: int) -> Operation:
        node: AVLBSTNode = Find(self.root, time)

        return None if node is None else node.operation

    def previous_bridge_time(self, time: int) -> int:
        return PreviousBridgeTime(self.root, 0, time)

    def next_bridge_time(self, time: int) -> int:
        return NextBridgeTime(self.root, 0, time)

    def operation_with_greatest_key_after_time(self, time: int) -> Operation:
        return OperationWithGreatestKeyAfterTime(self.root, 0, time)[1]


class AVLBSTNode(AVLNode):
    def __init__(self, operation: Operation = None):
        if not isinstance(operation, Operation):
            raise TypeError("operation is not a Operation")

        super().__init__(key=operation.time)

        self.operation: Operation = operation

        self.min_time = operation.time
        self.max_time = operation.time

        self.sum: int = operation.type
        self.min_sum: int = operation.type
        self.max_sum: int = operation.type
        self.insert_operation: Tuple[int, Operation] = (
            (operation.key, operation) if operation.type == 1 else (-inf, None)
        )
        self.max_operation: Tuple[int, Operation] = self.insert_operation

    def update(self):
        super().update()

        self.min_time = self.min_key
        self.max_time = self.max_key

        self.sum = Sum(self.L) + self.operation.type + Sum(self.R)
        self.min_sum = min(
            MinSum(self.L),
            Sum(self.L) + self.operation.type + min(0, MinSum(self.R)),
        )
        self.max_sum = max(
            MaxSum(self.L),
            Sum(self.L) + self.operation.type + max(0, MaxSum(self.R)),
        )
        self.max_operation = max(
            MaxOperation(self.L),
            max(self.insert_operation, MaxOperation(self.R)),
        )

    @property
    def type(self):
        return self.operation.type

    @property
    def time(self):
        return self.operation.time


def Sum(node: AVLBSTNode) -> int:
    return 0 if node is None else node.sum


def MinSum(node: AVLBSTNode) -> int:
    return inf if node is None else node.min_sum


def MaxSum(node: AVLBSTNode) -> int:
    return -inf if node is None else node.max_sum


def MinTime(node: AVLBSTNode) -> int:
    return inf if node is None else node.min_time


def MaxTime(node: AVLBSTNode) -> int:
    return -inf if node is None else node.max_time


def MaxOperation(node: AVLBSTNode) -> Tuple[int, Operation]:
    return (-inf, None) if node is None else node.max_operation


def PreviousBridgeTime(node: AVLBSTNode, left_sum: int, time: int) -> int:
    if node is None:
        return -inf

    L_sum = left_sum + MinSum(node)
    R_sum = left_sum + MaxSum(node)

    if 0 < L_sum or R_sum < 0:
        return -inf

    if time < MinTime(node):
        return -inf

    candidate = PreviousBridgeTime(
        node.R, left_sum + Sum(node.L) + node.type, time
    )
    if candidate != -inf:
        return candidate

    if node.time <= time and left_sum + Sum(node.L) + node.type == 0:
        return node.time

    return PreviousBridgeTime(node.L, left_sum, time)


def NextBridgeTime(node: AVLBSTNode, left_sum: int, time: int) -> int:
    if node is None:
        return inf

    L_sum = left_sum + MinSum(node)
    R_sum = left_sum + MaxSum(node)

    if 0 < L_sum or R_sum < 0:
        return inf

    if MaxTime(node) < time:
        return inf

    candidate = NextBridgeTime(node.L, left_sum, time)
    if candidate != inf:
        return candidate

    if node.time >= time and left_sum + Sum(node.L) + node.type == 0:
        return node.time

    return NextBridgeTime(node.R, left_sum + Sum(node.L) + node.type, time)


def OperationWithGreatestKeyAfterTime(
    node: AVLBSTNode,
    left_sum: int,
    time: int,
) -> Tuple[int, Operation]:
    if node is None:
        return (-inf, None)

    if MaxTime(node) < time:
        return (-inf, None)

    if time <= MinTime(node):
        return MaxOperation(node)

    if node.time < time:
        return OperationWithGreatestKeyAfterTime(
            node.R, left_sum + Sum(node.L) + node.type, time
        )

    return max(
        OperationWithGreatestKeyAfterTime(node.L, left_sum, time),
        max(
            node.insert_operation,
            OperationWithGreatestKeyAfterTime(
                node.R, left_sum + Sum(node.L) + node.type, time
            ),
        ),
    )
