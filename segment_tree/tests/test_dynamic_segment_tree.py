import unittest
from typing import List

from segment_tree.dynamic.dynamic_segment_tree import DynamicSegmentTree
from segment_tree.dynamic.interface import (
    Insert,
    NewDynamicSegmentTree,
    Segments,
)
from segment_tree.segment import Segment


class TestDynamicSegmentTree(unittest.TestCase):
    def __check__(
        self,
        dynamic_segment_tree: DynamicSegmentTree,
        segments: List[Segment],
        left: int,
        right: int,
    ):
        for i in range(left, right + 1):
            answer_segments: List[Segment] = []

            for segment in segments:
                if segment.includes(i):
                    answer_segments.append(segment)

            self.assertEqual(
                set(Segments(dynamic_segment_tree, i)), set(answer_segments)
            )

    def test_dynamic_segment_tree(self):
        dynamic_segment_tree = NewDynamicSegmentTree()
        segments: List[Segment] = []

        def __insert__(left: int, right: int):
            segment = Segment(left, right)
            segments.append(segment)
            Insert(dynamic_segment_tree, segment)

            self.__check__(dynamic_segment_tree, segments, 0, 100)

        __insert__(10, 50)
        __insert__(80, 90)
        __insert__(55, 75)
        __insert__(5, 14)
        __insert__(33, 66)
        __insert__(5, 5)
        __insert__(2, 22)
        __insert__(50, 120)
