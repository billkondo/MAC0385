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
