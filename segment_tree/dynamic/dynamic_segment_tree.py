from typing import Dict, List

from segment_tree.segment import Segment
from segment_tree.static.static_segment_tree import StaticSegmentTree


class DynamicSegmentTree:
    def __init__(self):
        self.segment_trees: Dict[int, StaticSegmentTree] = {}
        self.sizes: Dict[int, int] = {}

    def insert(self, segment: Segment):
        size = 1
        segments: List[Segment] = [segment]

        while self.sizes.get(size) is not None:
            segments += self.segment_trees[size].segments

            self.sizes.pop(size)
            self.segment_trees.pop(size)
            size *= 2

        self.segment_trees[size] = StaticSegmentTree(segments)
        self.sizes[size] = 1

    def find(self, x: int) -> List[Segment]:
        segments: List[Segment] = []

        for size in self.sizes.keys():
            segments += self.segment_trees[size].find(x)

        return list(set(segments))
