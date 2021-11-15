from typing import List


def build_lcp_array(
    text: str,
    suffix_array: List[int],
) -> List[int]:
    _text = text + "$"
    lcp_array: List[int] = []

    lcp_array.append(0)
    for i in range(1, len(suffix_array)):
        lcp_array.append(
            __compute_lcp(
                _text[suffix_array[i - 1] :],
                _text[suffix_array[i] :],
            ),
        )

    return lcp_array


def __compute_lcp(x: str, y: str) -> int:
    lcp = 0

    while lcp < min(len(x), len(y)) and x[lcp] == y[lcp]:
        lcp += 1

    return lcp
