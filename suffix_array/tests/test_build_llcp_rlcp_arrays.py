import unittest

from suffix_array import build_llcp_rlcp_arrays


class TestBuildLLCPRLCPArrays(unittest.TestCase):
    def test_build_llcp_rlcp_arrays(self):
        lcp_array = [0, 1, 4, 1, 1, 0, 3, 0, 0, 0, 2]
        llcp, rlcp = build_llcp_rlcp_arrays(lcp_array)

        self.assertEqual(llcp, [0, 0, 4, 1, 0, 0, 3, 0, 0, 0, 0])
        self.assertEqual(rlcp, [1, 1, 1, 1, 0, 0, 0, 0, 0, 2, 0])
