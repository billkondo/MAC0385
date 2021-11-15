from typing import List, Tuple


def build_llcp_rlcp_arrays(
    lcp: List[int],
) -> Tuple[List[int], List[int]]:
    n = len(lcp)
    llcp = [0] * (n)
    rlcp = [0] * (n)

    __lrlcp([0] + lcp, llcp, rlcp, 0, n)

    return llcp[1:] + [0], rlcp[1:] + [0]


def __lrlcp(
    lcp: List[int],
    llcp: List[int],
    rlcp: List[int],
    i: int,
    j: int,
    side: str = None,
):
    value = 0

    if i == j - 1:
        value = lcp[j]
    else:
        m = (i + j) // 2
        __lrlcp(lcp, llcp, rlcp, i, m, "L")
        __lrlcp(lcp, llcp, rlcp, m, j, "R")
        value = min(llcp[m], rlcp[m])

    if side == "L":
        llcp[j] = value

    if side == "R":
        rlcp[i] = value
