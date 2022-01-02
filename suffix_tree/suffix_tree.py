from typing import Dict, List, Tuple

from suffix_array import build_lcp_array_linear, build_suffix_array_linear

from .suffix_tree_node import SuffixTreeNode


class SuffixTree:
    def __init__(self, text: str):
        self._text = text + "$"
        self._suffix_array = build_suffix_array_linear(text)
        self._lcp_array = build_lcp_array_linear(text, self._suffix_array)
        self.alphabet = self._build_alphabet()

        self.root = self._build()
        self._fill_node_fields(self.root)

    def _build_alphabet(self) -> Dict[str, int]:
        """
        Find letters from text and build a dictionary that maps
        letters to their ranks (letter with rank 0 is the first in the alphabet)
        """

        alphabet: Dict[str, int] = {}
        rank = 0
        marked_letters: Dict[str, bool] = {}
        letters = []

        for c in self._text:
            if not marked_letters.get(c):
                marked_letters[c] = True
                letters.append(c)

        letters.sort()
        for c in letters:
            alphabet[c] = rank
            rank += 1

        return alphabet

    def _build(self) -> SuffixTreeNode:
        """
        Build suffix tree and fill suffix_index field at the same time.
        Return the root of suffix tree.
        """

        stack: List[SuffixTreeNode] = []
        suffix_index = 0

        def _add_leaf(node: SuffixTreeNode):
            nonlocal suffix_index

            node.add_child(SuffixTreeNode(suffix_index=self._suffix_array[suffix_index]))
            suffix_index += 1

        for index in range(1, len(self._lcp_array)):
            lcp = self._lcp_array[index]

            if stack and stack[-1].lcp == lcp:
                _add_leaf(stack[-1])

            while stack and stack[-1].lcp > lcp:
                node = stack.pop()
                previous_node = stack[-1]

                previous_node.add_child(node)
                _add_leaf(node)

            if not stack or stack[-1].lcp != lcp:
                stack.append(SuffixTreeNode(lcp))
                _add_leaf(stack[-1])

        while len(stack) > 1:
            node = stack.pop()
            previous_node = stack[-1]

            previous_node.add_child(node)
            _add_leaf(node)

        assert suffix_index == len(self._suffix_array)

        return stack[-1]

    def _fill_node_fields(self, node: SuffixTreeNode, parent: SuffixTreeNode = None):
        """
        Compute start, end and num_leaves fields for each node in suffix tree.
        Position children in their correct indexes for each internal node.
        """

        for child in node.children:
            self._fill_node_fields(child, node)
            node.num_leaves += child.num_leaves

        if node.is_leaf():
            node.end = len(self._text) - 1
            node.start = node.suffix_index + parent.lcp
            node.num_leaves = 1
        else:
            length = node.lcp - (parent.lcp if parent is not None else 0)
            node.end = node.children[1].start - 1
            node.start = node.end - length + 1
            self._reorder_children(node)

    def _reorder_children(self, node: SuffixTreeNode):
        ALPHABET_SIZE = len(self.alphabet.keys())
        children: List[SuffixTreeNode] = [None for _ in range(0, ALPHABET_SIZE)]

        for child in node.children:
            letter = self._text[child.start]
            children[self.alphabet[letter]] = child

        node.children = children

    def search(self, pattern: str) -> bool:
        _, pattern_fully_matched = self._find_last_node_that_matches_pattern(pattern)

        return pattern_fully_matched

    def ocurrences(self, pattern: str) -> List[int]:
        node, pattern_fully_matched = self._find_last_node_that_matches_pattern(pattern)

        if not pattern_fully_matched:
            return []

        leaves: List[int] = []
        self._find_node_leaves(node, leaves)

        return leaves

    def number_of_ocurrences(self, pattern: str) -> int:
        node, pattern_fully_matched = self._find_last_node_that_matches_pattern(pattern)

        if not pattern_fully_matched:
            return 0

        return node.num_leaves

    def _find_last_node_that_matches_pattern(self, pattern: str) -> Tuple[SuffixTreeNode, bool]:
        node = self.root
        index = 0

        while node and index < len(pattern):
            next_edge = self.alphabet.get(pattern[index], -1)
            letter_exists_in_alphabet = next_edge != -1

            if not letter_exists_in_alphabet or not node.children[next_edge]:
                break

            node = node.children[next_edge]

            def try_match_pattern_with_suffix_link() -> bool:
                nonlocal index

                i = node.start
                while i <= node.end and index < len(pattern):
                    if pattern[index] == self._text[i]:
                        i += 1
                        index += 1
                    else:
                        break

                return i > node.end

            pattern_fully_matched_suffix_link = try_match_pattern_with_suffix_link()
            if not pattern_fully_matched_suffix_link:
                break

        pattern_fully_matched = index == len(pattern)
        return node, pattern_fully_matched

    def _find_node_leaves(self, node: SuffixTreeNode, leaves: List[int]):
        if not node:
            return

        if node.is_leaf():
            leaves.append(node.suffix_index)
            return

        for child in node.children:
            self._find_node_leaves(child, leaves)

    def print(self) -> List[str]:
        nodes: List[str] = []
        self._pre_order_traversal(self.root, nodes)

        return nodes

    def _pre_order_traversal(self, node: SuffixTreeNode, nodes: List[SuffixTreeNode]):
        if not node:
            return

        if node is not self.root:
            nodes.append(f"[{node.start}, {node.end}]")

        for child in node.children:
            self._pre_order_traversal(child, nodes)
