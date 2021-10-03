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

    def test_segment_hash(self):
        self.assertEqual(Segment(1, 2), Segment(1, 2))
        self.assertNotEqual(Segment(10, 20), Segment(10, 30))

    def test_segment_set(self):
        self.assertEqual(
            set(
                [
                    Segment(1, 2),
                    Segment(0, 10),
                    Segment(1, 2),
                ]
            ),
            set(
                [
                    Segment(0, 10),
                    Segment(1, 2),
                    Segment(0, 10),
                ],
            ),
        )

    def test_includes(self):
        self.assertTrue(Segment(5, 10).includes(7))
        self.assertFalse(Segment(10, 20).includes(25))
        self.assertTrue(Segment(100, 200).includes(100))
        self.assertTrue(Segment(1, 1).includes(1))
