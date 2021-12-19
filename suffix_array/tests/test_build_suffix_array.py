import unittest
from typing import List

from parameterized import parameterized, parameterized_class
from suffix_array import build_suffix_array, build_suffix_array_linear


@parameterized_class(
    [
        {
            "build_suffix_array": lambda _: build_suffix_array,
        },
        {
            "build_suffix_array": lambda _: build_suffix_array_linear,
        },
    ]
)
class TestBuildSuffixArray(unittest.TestCase):
    def _build_suffix_array(self, text: str) -> List[int]:
        callback = self.build_suffix_array()
        return callback(text)

    @parameterized.expand(
        [
            ["banana", [6, 5, 3, 1, 0, 4, 2]],
            ["abracadabra", [11, 10, 7, 0, 3, 5, 8, 1, 4, 6, 9, 2]],
            ["AAACCTTTGCGACC", [14, 0, 1, 11, 2, 13, 12, 3, 9, 4, 10, 8, 7, 6, 5]],
            ["AAAAAAAAAA", [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]],
            ["AAAAAAAAA", [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]],
            ["AAAAAAAA", [8, 7, 6, 5, 4, 3, 2, 1, 0]],
            ["AAAAAAA", [7, 6, 5, 4, 3, 2, 1, 0]],
            ["AAAAAA", [6, 5, 4, 3, 2, 1, 0]],
            ["AAAAA", [5, 4, 3, 2, 1, 0]],
            ["AAAA", [4, 3, 2, 1, 0]],
            ["AAA", [3, 2, 1, 0]],
            ["01", [2, 0, 1]],
        ]
    )
    def test_build_suffix_array(self, text: str, expected: str):
        suffix_array = self._build_suffix_array(text)

        self.assertEqual(suffix_array, expected)
