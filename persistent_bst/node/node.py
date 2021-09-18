class Node:
    def __init__(self, value):
        if value is None:
            raise ValueError("value is empty")

        self.value = value
        self.left: Node = None
        self.right: Node = None
