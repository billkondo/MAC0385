import unittest

from segment_tree.segment import Segment


class TestSegment(unittest.TestCase):
    def test_segment(self):
        self.assertRaises(TypeError, lambda: Segment(left="10"))
        self.assertRaises(TypeError, lambda: Segment(left=10, right="10"))
        self.assertRaises(ValueError, lambda: Segment(10, 5))

        segment = Segment(10, 15)
        self.assertEqual(segment.left, 10)
        self.assertEqual(segment.right, 15)
