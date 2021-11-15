from typing import List, Tuple

from .build_lcp_array import build_lcp_array
from .build_llcp_rlcp_arrays import build_llcp_rlcp_arrays
from .build_suffix_array import build_suffix_array


class SuffixArray:
    def __init__(self, text: str):
        self.__text = text + "$"
        self.__suffix_array = build_suffix_array(text)
        self.__lcp_array = build_lcp_array(text, self.__suffix_array)
        self.__llcp, self.__rlcp = build_llcp_rlcp_arrays(self.__lcp_array)

    def search(self, p: str) -> bool:
        _, match = self.__binary_search(p)
        return match == len(p)

    def ocurrences(self, p: str) -> List[int]:
        left_index, right_index = self.__ocurrences_range(p)

        suffixes = []
        for i in range(left_index, right_index + 1):
            suffixes.append(self.__suffix_array[i])

        return suffixes

    def number_ocurrences(self, p: str) -> int:
        left_index, right_index = self.__ocurrences_range(p)

        return right_index - left_index + 1

    def __ocurrences_range(self, p: str) -> Tuple[int, int]:
        left_index, lmatch = self.__binary_search(p)
        right_index, rmatch = self.__binary_search(p, True)

        assert lmatch == rmatch

        if lmatch == len(p):
            return left_index, right_index

        return 1, 0

    def print(self):
        print(self.__suffix_array)
        print(self.__lcp_array)

    def __binary_search(self, p: str, upper=False) -> Tuple[int, int]:
        L = 0
        R = len(self.__text)

        lmatch = 0
        rmatch = 0

        def __compare(M: int, start: int):
            if M >= len(self.__text):
                return start

            pointer = start
            while pointer < min(len(p), self.__suffix_length(M)) and p[pointer] == self.__suffix_char_at(M, pointer):
                pointer += 1

            return pointer

        def __next_iteration(M: int, start: int):
            nonlocal L
            nonlocal R
            nonlocal lmatch
            nonlocal rmatch

            next_match = __compare(M, start)

            if next_match == len(p):
                if upper:
                    L = M
                    lmatch = next_match
                else:
                    R = M
                    rmatch = next_match
            elif p[next_match] < self.__suffix_char_at(M, next_match):
                R = M
                rmatch = next_match
            else:
                L = M
                lmatch = next_match

        while L < R - 1:
            M = (L + R) // 2

            if lmatch == rmatch:
                __next_iteration(M, lmatch)
            elif lmatch > rmatch:
                if lmatch < self.__llcp[M]:
                    L = M
                elif self.__llcp[M] < lmatch:
                    R = M
                    rmatch = self.__llcp[M]
                else:
                    __next_iteration(M, lmatch)
            else:
                if rmatch < self.__rlcp[M]:
                    R = M
                elif self.__rlcp[M] < rmatch:
                    L = M
                    lmatch = self.__rlcp[M]
                else:
                    __next_iteration(M, rmatch)

        lmatch = __compare(L, lmatch)
        rmatch = __compare(R, rmatch)

        if lmatch > rmatch:
            return (L, lmatch)
        elif lmatch < rmatch:
            return (R, rmatch)
        else:
            return (R, rmatch) if upper else (L, lmatch)

    def __suffix_length(self, M: int) -> int:
        return len(self.__text) - self.__suffix_array[M]

    def __suffix_char_at(self, M: int, i: int):
        if i >= self.__suffix_length(M):
            return ""

        return self.__text[self.__suffix_array[M] + i]
