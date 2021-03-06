import unittest
from typing import List

from parameterized import parameterized
from suffix_tree import SuffixTree, SuffixTreeNode


class TestSuffixTree(unittest.TestCase):
    def _find_node_by_following_suffix_links(
        self,
        suffix_tree: SuffixTree,
        *links: List[str],
    ):
        node = suffix_tree.root
        for c in links:
            node = node.children[suffix_tree.alphabet[c]]

        return node

    def _assert_node_data(
        self,
        node: SuffixTreeNode,
        lcp: int,
        suffix_index: int,
        start: int,
        end: int,
        num_leaves: int,
    ):
        self.assertEqual(node.lcp, lcp)
        self.assertEqual(node.suffix_index, suffix_index)
        self.assertEqual(node.start, start)
        self.assertEqual(node.end, end)
        self.assertEqual(node.num_leaves, num_leaves)

    def test_suffix_tree_build(self):
        suffix_tree = SuffixTree("abracadabra")

        self._assert_node_data(self._find_node_by_following_suffix_links(suffix_tree), 0, -1, 0, -1, 12)
        self._assert_node_data(self._find_node_by_following_suffix_links(suffix_tree, "$"), -1, 11, 11, 11, 1)
        self._assert_node_data(self._find_node_by_following_suffix_links(suffix_tree, "a"), 1, -1, 0, 0, 5)
        self._assert_node_data(self._find_node_by_following_suffix_links(suffix_tree, "a", "$"), -1, 10, 11, 11, 1)
        self._assert_node_data(self._find_node_by_following_suffix_links(suffix_tree, "a", "b"), 4, -1, 1, 3, 2)
        self._assert_node_data(self._find_node_by_following_suffix_links(suffix_tree, "a", "b", "$"), -1, 7, 11, 11, 1)
        self._assert_node_data(self._find_node_by_following_suffix_links(suffix_tree, "a", "b", "c"), -1, 0, 4, 11, 1)
        self._assert_node_data(self._find_node_by_following_suffix_links(suffix_tree, "a", "c"), -1, 3, 4, 11, 1)
        self._assert_node_data(self._find_node_by_following_suffix_links(suffix_tree, "a", "d"), -1, 5, 6, 11, 1)
        self._assert_node_data(self._find_node_by_following_suffix_links(suffix_tree, "b"), 3, -1, 1, 3, 2)
        self._assert_node_data(self._find_node_by_following_suffix_links(suffix_tree, "b", "$"), -1, 8, 11, 11, 1)
        self._assert_node_data(self._find_node_by_following_suffix_links(suffix_tree, "b", "c"), -1, 1, 4, 11, 1)
        self._assert_node_data(self._find_node_by_following_suffix_links(suffix_tree, "c"), -1, 4, 4, 11, 1)
        self._assert_node_data(self._find_node_by_following_suffix_links(suffix_tree, "d"), -1, 6, 6, 11, 1)
        self._assert_node_data(self._find_node_by_following_suffix_links(suffix_tree, "r"), 2, -1, 2, 3, 2)
        self._assert_node_data(self._find_node_by_following_suffix_links(suffix_tree, "r", "$"), -1, 9, 11, 11, 1)
        self._assert_node_data(self._find_node_by_following_suffix_links(suffix_tree, "r", "c"), -1, 2, 4, 11, 1)

    @parameterized.expand(
        [
            ("abra", [7, 0], 2),
            ("ra", [9, 2], 2),
            ("a", [10, 7, 0, 3, 5], 5),
            ("d", [6], 1),
            ("abr", [7, 0], 2),
        ]
    )
    def test_suffix_tree_search(self, pattern: str, ocurrences: List[int], number_of_ocurrence: str):
        suffix_tree = SuffixTree("abracadabra")

        self.assertTrue(suffix_tree.search(pattern))
        self.assertEqual(suffix_tree.ocurrences(pattern), ocurrences)
        self.assertEqual(suffix_tree.number_of_ocurrences(pattern), number_of_ocurrence)

    def test_suffix_tree_not_found(self):
        suffix_tree = SuffixTree("abracadabra")

        self.assertFalse(suffix_tree.search("zebra"))
        self.assertEqual(suffix_tree.ocurrences("zebra"), [])
        self.assertEqual(suffix_tree.number_of_ocurrences("zebra"), 0)

    def test_suffix_tree_print(self):
        suffix_tree = SuffixTree("abracadabra")

        self.assertEqual(
            suffix_tree.print(),
            [
                "[11, 11]",
                "[0, 0]",
                "[11, 11]",
                "[1, 3]",
                "[11, 11]",
                "[4, 11]",
                "[4, 11]",
                "[6, 11]",
                "[1, 3]",
                "[11, 11]",
                "[4, 11]",
                "[4, 11]",
                "[6, 11]",
                "[2, 3]",
                "[11, 11]",
                "[4, 11]",
            ],
        )
