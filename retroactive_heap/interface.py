import math

from retroactive_heap.current_heap.current_heap import CurrentHeap
from retroactive_heap.heap import Heap
from retroactive_heap.operations_bst.bst import BST


def NewHeap(
    current_heap: CurrentHeap = None,
    operations_bst: BST = None,
) -> Heap:
    return Heap(
        current_heap=current_heap,
        operations_bst=operations_bst,
    )


def AddInsert(heap: Heap, time: int, key: int):
    previous_bridge_time = heap.operations_bst.previous_bridge_time(time)
    operation = heap.operations_bst.max(previous_bridge_time)

    if operation is None or operation.key < key:
        heap.operations_bst.insert(time, 0, key)
        heap.current_heap.insert(key, time)
    else:
        heap.operations_bst.insert(time, 1, key)

        heap.current_heap.insert(operation.key, operation.time)
        heap.operations_bst.delete(operation.key)
        heap.operations_bst.insert(operation.time, 0, operation.key)


def AddDeleteMin(heap: Heap, time: int):
    next_bridge_time = heap.operations_bst.next_bridge_time(time)
    minimum_node = heap.current_heap.min(next_bridge_time - 1)

    if minimum_node is None:
        raise RuntimeError(f"heap is empty at time {time}")

    heap.operations_bst.insert(time, -1)

    heap.current_heap.delete(minimum_node.key)
    heap.operations_bst.delete(minimum_node.time)
    heap.operations_bst.insert(minimum_node.time, +1, minimum_node.key)


def Delete(heap: Heap, time: int):
    operation = heap.operations_bst.find(time)

    if operation is None:
        raise RuntimeError(f"operation at time {time} was not found")

    if operation.type == -1:
        heap.operations_bst.delete(time)

        previous_bridge_time = heap.operations_bst.previous_bridge_time(time)
        operation = heap.operations_bst.max(previous_bridge_time)

        heap.current_heap.insert(operation.key, operation.time)
        heap.operations_bst.delete(operation.key)
        heap.operations_bst.insert(operation.time, 0, operation.key)
    else:
        if operation.type == 0:
            heap.current_heap.delete(time)
        else:
            next_bridge_time = heap.operations_bst.next_bridge_time(time)
            minimum_node = heap.current_heap.min(next_bridge_time - 1)

            if minimum_node is None:
                raise RuntimeError(
                    f"delete will be unmatched if insert at {time} is deleted"
                )

            heap.current_heap.delete(minimum_node.key)
            heap.operations_bst.delete(minimum_node.time)
            heap.operations_bst.insert(minimum_node.time, +1, minimum_node.key)

        heap.operations_bst.delete(time)


def Min(heap: Heap) -> int:
    min_node = heap.current_heap.min(math.inf)

    if min_node is not None:
        return min_node.key

    return min_node
