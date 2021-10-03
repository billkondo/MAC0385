from typing import List

from segment_tree.segment import Segment
from segment_tree.static.static_segment_tree import StaticSegmentTree


def NewStaticSegmentTree(segments: List[Segment]) -> StaticSegmentTree:
    return StaticSegmentTree(segments)


def Segments(static_segment_tree: StaticSegmentTree, x: int) -> List[Segment]:
    return static_segment_tree.find(x)
