from typing import List

from segment_tree.dynamic.dynamic_segment_tree import DynamicSegmentTree
from segment_tree.segment import Segment


def NewDynamicSegmentTree():
    return DynamicSegmentTree()


def Insert(dynamic_segment_tree: DynamicSegmentTree, segment: Segment):
    dynamic_segment_tree.insert(segment)


def Segments(
    dynamic_segment_tree: DynamicSegmentTree, x: int
) -> List[Segment]:
    return dynamic_segment_tree.find(x)
