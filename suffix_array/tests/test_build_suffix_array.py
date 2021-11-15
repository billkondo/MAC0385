import unittest

from parameterized import parameterized_class
from suffix_array import build_suffix_array


@parameterized_class(
    [
        {
            "text": "banana",
            "expected": [6, 5, 3, 1, 0, 4, 2],
        },
        {
            "text": "abracadabra",
            "expected": [11, 10, 7, 0, 3, 5, 8, 1, 4, 6, 9, 2],
        },
        {
            "text": "AAACCTTTGCGACC",
            "expected": [14, 0, 1, 11, 2, 13, 12, 3, 9, 4, 10, 8, 7, 6, 5],
        },
    ]
)
class TestBuildSuffixArray(unittest.TestCase):
    def test_build_suffix_array(self):
        suffix_array = build_suffix_array(self.text)

        self.assertEqual(suffix_array, self.expected)
