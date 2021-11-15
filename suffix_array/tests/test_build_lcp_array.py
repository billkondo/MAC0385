import unittest

from parameterized import parameterized_class
from suffix_array import build_lcp_array, build_suffix_array


@parameterized_class(
    [
        {
            "text": "banana",
            "expected": [0, 0, 1, 3, 0, 0, 2],
        },
        {
            "text": "abracadabra",
            "expected": [0, 0, 1, 4, 1, 1, 0, 3, 0, 0, 0, 2],
        },
        {
            "text": "AAACCTTTGCGACC",
            "expected": [0, 0, 2, 1, 3, 0, 1, 2, 1, 1, 0, 1, 0, 1, 2],
        },
    ]
)
class TestBuildLCPArray(unittest.TestCase):
    def test_build_lcp_array_01(self):
        suffix_array = build_suffix_array(self.text)
        lcp_array = build_lcp_array(self.text, suffix_array)

        self.assertEqual(lcp_array, self.expected)
