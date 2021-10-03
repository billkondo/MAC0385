class Segment:
    def __init__(self, left=None, right=None):
        if not isinstance(left, int):
            raise TypeError("left is not a int")

        if not isinstance(right, int):
            raise TypeError("right is not a int")

        if left > right:
            raise ValueError("left is greater than right")

        self.left: int = left
        self.right: int = right
