from typing import List

from segment_tree.segment import Segment


class Node:
    def __init__(self, left=None, right=None):
        self.segment = Segment(left, right)
        self.segments: List[Segment] = []

        self.L: Node = None
        self.R: Node = None

    @property
    def left(self):
        return self.segment.left

    @property
    def right(self):
        return self.segment.right

    def __str__(self) -> str:
        return f"{self.segment} {self.segments}"
