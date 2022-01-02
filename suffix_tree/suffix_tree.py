from typing import Dict, List

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
