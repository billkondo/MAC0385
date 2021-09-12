from retroactive_stack.bst.bst import BST
from retroactive_stack.bst.simple_bst import SimpleBST


class Stack:
    def __init__(self, bst=None):
        if not isinstance(bst, BST):
            raise TypeError("value is not a BST")

        self.bst: BST = SimpleBST() if bst is None else bst
