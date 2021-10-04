from bisect import bisect_left
from math import inf
from typing import Dict, List

from segment_tree.node import Node
from segment_tree.segment import Segment


class StaticSegmentTree:
    def __init__(self, segments: List[Segment] = []):
        self.n = 0
        self.endpoints: List[int] = []
        self.endpoints_map: Dict[int, int] = {}
        self.root: Node = None
        self.segments: List[Segment] = segments

        for segment in segments:
            self.endpoints.append(segment.left)
            self.endpoints.append(segment.right)

        self.endpoints.append(-inf)
        self.endpoints.append(inf)
        self.endpoints = list(set(self.endpoints))
        self.endpoints.sort()

        for endpoint in self.endpoints:
            self.n += 1
            self.endpoints_map[endpoint] = self.n

        self.root = self.__build__(1, self.n)
        for segment in segments:
            self.__insert__(
                self.root,
                1,
                self.n,
                self.endpoints_map[segment.left],
                self.endpoints_map[segment.right],
                segment,
            )

    def __build__(self, left: int, right: int) -> Node:
        node = Node(left, right)

        if left == right:
            return node

        mid = (left + right) // 2

        node.L = self.__build__(left, mid)
        node.R = self.__build__(mid + 1, right)

        return node

    def __insert__(
        self,
        node: Node,
        left: int,
        right: int,
        L: int,
        R: int,
        segment: Segment,
    ):
        if right < L or R < left:
            return

        if L <= left and right <= R:
            node.segments.append(segment)
            return

        mid = (left + right) // 2
        self.__insert__(node.L, left, mid, L, R, segment)
        self.__insert__(node.R, mid + 1, right, L, R, segment)

    def __find__(
        self, node: Node, left: int, right: int, leaf: int, x: int
    ) -> List[Segment]:
        if node is None:
            return []

        if leaf < left or right < leaf:
            return []

        mid = (left + right) // 2

        segments = self.__find__(node.L, left, mid, leaf, x) + self.__find__(
            node.R, mid + 1, right, leaf, x
        )

        if left <= leaf and leaf <= right:
            for segment in node.segments:
                if segment.includes(x):
                    segments.append(segment)

        return segments

    def find(self, x: int) -> List[Segment]:
        index = bisect_left(self.endpoints, x) + 1

        if self.endpoints_map.get(x) is not None:
            return list(
                set(
                    self.__find__(
                        self.root,
                        1,
                        self.n,
                        index,
                        x,
                    ),
                )
            )

        return list(
            set(
                self.__find__(
                    self.root,
                    1,
                    self.n,
                    index - 1,
                    x,
                )
                + self.__find__(
                    self.root,
                    1,
                    self.n,
                    index,
                    x,
                ),
            )
        )

    def print(self):
        self.__print__(self.root)

    def __print__(self, node: Node):
        if node is None:
            return

        print(str(node))

        self.__print__(node.L)
        self.__print__(node.R)
