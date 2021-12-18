import unittest
from typing import List

from parameterized import parameterized, parameterized_class
from suffix_array import build_lcp_array, build_lcp_array_linear, build_suffix_array


@parameterized_class(
    [
        {
            "build_lcp_array": lambda _: build_lcp_array,
        },
        {
            "build_lcp_array": lambda _: build_lcp_array_linear,
        },
    ]
)
class TestBuildLCPArray(unittest.TestCase):
    def _build_lcp_array(self, text: str, suffix_array: List[int]) -> List[int]:
        callback = self.build_lcp_array()
        return callback(text, suffix_array)

    @parameterized.expand(
        [
            ["banana", [0, 0, 1, 3, 0, 0, 2]],
            ["abracadabra", [0, 0, 1, 4, 1, 1, 0, 3, 0, 0, 0, 2]],
            ["AAACCTTTGCGACC", [0, 0, 2, 1, 3, 0, 1, 2, 1, 1, 0, 1, 0, 1, 2]],
        ]
    )
    def test_build_lcp_array_01(self, text: str, expected: List[int]):
        suffix_array = build_suffix_array(text)
        lcp_array = self._build_lcp_array(text, suffix_array)

        self.assertEqual(lcp_array, expected)
