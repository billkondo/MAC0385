from retroactive_heap.current_heap.current_heap import CurrentHeap
from retroactive_heap.current_heap.simple_current_heap import SimpleCurrentHeap
from retroactive_heap.operations_bst.bst import BST
from retroactive_heap.operations_bst.simple_bst import SimpleBST


class Heap:
    def __init__(
        self,
        current_heap: CurrentHeap = None,
        operations_bst: BST = None,
    ):
        if current_heap is not None and not isinstance(
            current_heap, CurrentHeap
        ):
            raise TypeError("current_heap is not a CurrentHeap")

        if operations_bst is not None and not isinstance(operations_bst, BST):
            raise TypeError("operations_bst is not a BST")

        self.current_heap: CurrentHeap = (
            SimpleCurrentHeap() if current_heap is None else current_heap
        )
        self.operations_bst: BST = (
            SimpleBST() if operations_bst is None else operations_bst
        )
