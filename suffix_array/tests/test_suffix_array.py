import unittest

from suffix_array import SuffixArray


class TestSuffixArray(unittest.TestCase):
    def test_suffix_array(self):
        suffix_array = SuffixArray("abracadabra")

        self.assertTrue(suffix_array.search("abra"))
        self.assertEqual(suffix_array.ocurrences("abra"), [7, 0])
        self.assertEqual(suffix_array.number_ocurrences("abra"), 2)

    def test_suffix_array_not_found(self):
        suffix_array = SuffixArray("abracadabra")

        self.assertFalse(suffix_array.search("zebra"))
        self.assertEqual(suffix_array.ocurrences("zebra"), [])
        self.assertEqual(suffix_array.number_ocurrences("zebra"), 0)

    def test_suffix_array_matches_in_array_suffix(self):
        suffix_array = SuffixArray("abracadabra")

        self.assertTrue(suffix_array.search("ra"))
        self.assertEqual(suffix_array.ocurrences("ra"), [9, 2])
        self.assertEqual(suffix_array.number_ocurrences("ra"), 2)

    def test_suffix_array_match_one_letter(self):
        suffix_array = SuffixArray("abracadabra")

        self.assertTrue(suffix_array.search("a"))
        self.assertEqual(suffix_array.ocurrences("a"), [10, 7, 0, 3, 5])
        self.assertEqual(suffix_array.number_ocurrences("a"), 5)

    def test_suffix_array_one_match(self):
        suffix_array = SuffixArray("abracadabra")

        self.assertTrue(suffix_array.search("d"))
        self.assertEqual(suffix_array.ocurrences("d"), [6])
        self.assertEqual(suffix_array.number_ocurrences("d"), 1)
