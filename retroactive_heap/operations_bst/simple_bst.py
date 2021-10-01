import math
from typing import List

from retroactive_heap.operations_bst.bst import BST
from retroactive_heap.operations_bst.operation import Operation


class SimpleBST(BST):
    def __init__(self):
        self.bst: List[Operation] = []

    def insert(self, time: int = None, type: int = None, key: int = None):
        self.bst.append(
            Operation(
                time=time,
                type=type,
                key=key,
            )
        )
        self.bst.sort(key=lambda operation: operation.time)

    def delete(self, time: int):
        self.bst = [
            operation for operation in self.bst if operation.time != time
        ]

    def find(self, time: int):
        for operation in self.bst:
            if operation.time == time:
                return operation

        return None

    def previous_bridge_time(self, time: int) -> int:
        bridge_time = -math.inf

        sum = 0
        for operation in self.bst:
            sum += operation.type

            if operation.time <= time and sum == 0:
                bridge_time = max(bridge_time, operation.time)

        return bridge_time

    def next_bridge_time(self, time: int) -> int:
        bridge_time = math.inf

        sum = 0
        for operation in self.bst:
            sum += operation.type

            if operation.time >= time and sum == 0:
                bridge_time = min(bridge_time, operation.time)

        return bridge_time

    def operation_with_greatest_key_after_time(self, time: int) -> Operation:
        max_operation: Operation = None

        for operation in self.bst:
            if operation.time >= time and operation.type == 1:
                if max_operation is None or max_operation.key < operation.key:
                    max_operation = operation

        return max_operation
