import unittest
from typing import List, Set

from segment_tree.segment import Segment
from segment_tree.static.interface import NewStaticSegmentTree, Segments


class TestStaticSegmentTree(unittest.TestCase):
    def test_static_segment_tree_01(self):
        segments: List[Segment] = [
            Segment(1, 5),
            Segment(2, 4),
            Segment(3, 4),
            Segment(3, 7),
            Segment(4, 9),
            Segment(6, 10),
        ]
        static_segment_tree = NewStaticSegmentTree(segments)

        def __segments__(x: int) -> Set[Segment]:
            return set(Segments(static_segment_tree, x))

        self.assertEqual(
            __segments__(0),
            set([]),
        )
        self.assertEqual(
            __segments__(1),
            set(
                [
                    Segment(1, 5),
                ],
            ),
        )
        self.assertEqual(
            __segments__(2),
            set(
                [
                    Segment(1, 5),
                    Segment(2, 4),
                ]
            ),
        )
        self.assertEqual(
            __segments__(3),
            set(
                [
                    Segment(2, 4),
                    Segment(3, 7),
                    Segment(3, 4),
                    Segment(1, 5),
                ]
            ),
        )
        self.assertEqual(
            __segments__(4),
            set(
                [
                    Segment(2, 4),
                    Segment(3, 7),
                    Segment(3, 4),
                    Segment(1, 5),
                    Segment(4, 9),
                ]
            ),
        )
        self.assertEqual(
            __segments__(5),
            set(
                [
                    Segment(3, 7),
                    Segment(1, 5),
                    Segment(4, 9),
                ]
            ),
        )
        self.assertEqual(
            __segments__(6),
            set(
                [
                    Segment(3, 7),
                    Segment(4, 9),
                    Segment(6, 10),
                ]
            ),
        )
        self.assertEqual(
            __segments__(7),
            set(
                [
                    Segment(3, 7),
                    Segment(4, 9),
                    Segment(6, 10),
                ]
            ),
        )
        self.assertEqual(
            __segments__(8),
            set(
                [
                    Segment(4, 9),
                    Segment(6, 10),
                ]
            ),
        )
        self.assertEqual(
            __segments__(9),
            set(
                [
                    Segment(4, 9),
                    Segment(6, 10),
                ],
            ),
        )
        self.assertEqual(
            __segments__(10),
            set(
                [
                    Segment(6, 10),
                ]
            ),
        )
        self.assertEqual(
            __segments__(11),
            set([]),
        )

    def test_static_segment_tree_02(self):
        segments = [
            Segment(10, 30),
            Segment(20, 50),
            Segment(25, 45),
        ]
        static_segment_tree = NewStaticSegmentTree(segments)

        for i in range(0, 55):
            query_segments = Segments(static_segment_tree, i)

            answer_segments = []
            for k in segments:
                if k.includes(i):
                    answer_segments.append(k)

            self.assertEqual(set(query_segments), set(answer_segments))
