from dataclasses import dataclass
from typing import List


def build_suffix_array(text: str) -> List[int]:
    _text = text + "$"
    suffixes: List[Suffix] = []

    for i in range(0, len(_text)):
        suffixes.append(
            Suffix(
                substring=_text[i:],
                l=i,
                r=len(_text) - 1,
            ),
        )

    suffixes.sort()

    return list(
        map(
            lambda suffix: suffix.l,
            suffixes,
        ),
    )


@dataclass(order=True)
class Suffix:
    substring: str
    l: int
    r: int
