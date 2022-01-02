from typing import List


class SuffixTreeNode:
    """
    Stores data for building and querying a suffix tree.

    If node is a leaf, then suffix_index should different than -1 and lcp should be -1.

    If node is internal, then lcp should be different than -1 and suffix_index should be -1.
    """

    def __init__(
        self,
        lcp: int = -1,
        suffix_index: int = -1,
    ):
        self.lcp: int = lcp
        self.suffix_index: int = suffix_index
        self.children: List[SuffixTreeNode] = []

        self.start: int = -1
        self.end: int = -1
        self.num_leaves = 0

    def add_child(self, node=None):
        if node is not None and not isinstance(node, SuffixTreeNode):
            raise ValueError(f"{node=} is not None neither an instance of SuffixTreeNode")

        self.children.append(node)

    def is_leaf(self) -> bool:
        return not self.children

    def is_empty(self) -> bool:
        return self.suffix_index == -1 and self.lcp == -1
