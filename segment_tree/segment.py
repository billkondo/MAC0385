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

    def includes(self, x: int) -> bool:
        return self.left <= x and x <= self.right

    def __eq__(self, other) -> bool:
        if not isinstance(other, Segment):
            return False

        return self.left == other.left and self.right == other.right

    def __hash__(self) -> int:
        return hash((self.left, self.right))

    def __str__(self) -> str:
        return f"[{self.left}, {self.right}]"

    def __repr__(self) -> str:
        return f"Segment({self.left}, {self.right})"
