from typing import List


def build_lcp_array_linear(text: str, suffix_array: List[int]) -> List[int]:
    _text = text + "$"
    n = len(_text)
    rank = [0 for i in range(0, n)]
    lcp_array = [0 for i in range(0, n)]

    assert n == len(suffix_array)

    for i in range(0, n):
        rank[suffix_array[i]] = i

    h = 0
    for i in range(0, n):
        if rank[i] > 0:
            j = suffix_array[rank[i] - 1]
            assert i != j

            while _text[i + h] == _text[j + h]:
                h = h + 1

            lcp_array[rank[i]] = h

            if h > 0:
                h = h - 1

    return lcp_array
