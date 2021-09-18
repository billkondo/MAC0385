from persistent_bst.node.node import Node


class BST:
    def __init__(self, root: Node = None):
        if root is not None and type(root) != Node:
            raise TypeError("root is not a Node")

        self.root = root
