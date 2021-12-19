from typing import Dict, List


def build_suffix_array_linear(text: str) -> List[int]:
    alphabet = _build_alphabet(text)
    alphabet["$"] = 0
    text += "$"
    modified_text: List[int] = [alphabet[c] for c in text]

    return _build_suffix_array_recursive(modified_text[:])


def _build_alphabet(text: str) -> Dict[str, int]:
    marked_characters: Dict[str, bool] = {}
    alphabet: Dict[str, int] = {}
    alphabet_size = 0
    characters = []

    for c in text:
        if not marked_characters.get(c):
            marked_characters[c] = True
            characters.append(c)

    characters.sort()
    for c in characters:
        alphabet[c] = alphabet_size + 1
        alphabet_size += 1

    return alphabet


def _build_suffix_array_recursive(text: List[int]) -> List[int]:
    n = len(text)

    # Base case: build suffix array using brute force solution
    if n <= 3:
        return _build_suffix_array_brute_force(text[:])

    text.append(0)
    text.append(0)

    T0_T1 = _build_T0_T1(text[:])  # Passing text[:] prevent passing it by reference
    suffix_array_T0_T1 = _build_suffix_array_recursive(T0_T1[:])

    i = 0
    j = 0
    intial_suffix_array_T2 = []

    for i in range(0, len(T0_T1)):
        if 0 < suffix_array_T0_T1[i] and suffix_array_T0_T1[i] <= (len(T0_T1) - 1) // 2:
            intial_suffix_array_T2.append(suffix_array_T0_T1[i])
            j += 1

    suffix_array_T2 = _counting_sort_T2(text[:], intial_suffix_array_T2)

    return _merge(text, suffix_array_T0_T1, suffix_array_T2)


def _build_suffix_array_brute_force(text: List[int]) -> List[int]:
    def _compare_suffixes(i: int, j: int) -> int:
        len_i = len(text) - i
        len_j = len(text) - j

        k = 0
        while k < len_i and k < len_j:
            if text[i + k] < text[j + k]:
                return -1

            if text[i + k] > text[j + k]:
                return 1

            k += 1

        return -1 if len_i < len_j else 1

    suffixes = [i for i in range(0, len(text))]

    # Inversion sort
    for i in range(1, len(text)):
        j = i
        while j > 0 and _compare_suffixes(suffixes[j - 1], suffixes[j]) > 0:
            suffixes[j - 1], suffixes[j] = suffixes[j], suffixes[j - 1]
            j -= 1

    return suffixes


def _compare_triples(text: List[int], i: int, j: int) -> int:
    for k in range(0, 3):
        if text[i + k] < text[j + k]:
            return -1

        if text[i + k] > text[j + k]:
            return 1

    return -1 if i > j else 0 if i == j else 1


def _max_letter_in_text(text: List[int]) -> int:
    MAX_LETTER = 0
    for c in text:
        MAX_LETTER = max(MAX_LETTER, c)

    return MAX_LETTER


def _build_T0_T1(text: List[int]) -> List[int]:
    def _sort_text_triples(text: List[int]) -> List[int]:
        MAX_LETTER = _max_letter_in_text(text)
        n = len(text)

        def _sort_triples_by_kth_letter(triples: List[int], k: int) -> List[int]:
            sorted_triples: List[int] = []
            buckets: List[int] = [[] for _ in range(0, MAX_LETTER + 1)]

            for i in range(0, n - 2):
                buckets[text[triples[i] + k]].append(triples[i])

            for bucket in list(reversed(buckets)):
                sorted_triples.extend(bucket)

            return sorted_triples

        triples = [i for i in range(0, n - 2)]
        for k in reversed(range(0, 3)):
            triples = _sort_triples_by_kth_letter(triples, k)

        return list(reversed(triples))

    def _build_rank(triples: int) -> List[int]:
        rank = [0 for _ in range(0, len(triples))]

        for i in range(0, len(triples)):
            rank[triples[i]] = i

        return rank

    def _concatenate_T0_and_T1(rank: List[int]) -> List[int]:
        T0_T1 = []
        n = len(rank)

        for i in range(0, n, 3):
            T0_T1.append(rank[i])

        for i in range(1, n, 3):
            T0_T1.append(rank[i])

        return T0_T1

    triples = _sort_text_triples(text)
    rank = _build_rank(triples)

    return _concatenate_T0_and_T1(rank)


def _counting_sort_T2(text: List[int], initial_suffix_array_T2: List[int]) -> List[int]:
    def _sort_initial_suffix_array_T2_by_first_letter(initial_suffix_array_T2: List[int]) -> List[int]:
        MAX_LETTER = _max_letter_in_text(text)
        buckets = [[] for _ in range(0, MAX_LETTER + 1)]

        for i in range(0, len(initial_suffix_array_T2)):
            buckets[text[3 * initial_suffix_array_T2[i] - 1]].append(initial_suffix_array_T2[i] - 1)

        suffix_array = []
        for bucket in buckets:
            suffix_array.extend(bucket)

        return suffix_array

    def _add_last_triple(suffix_array: List[int], text: List[int]) -> List[int]:
        if len(text) % 3 != 2:
            # Last triple is not in T2 or was already inserted
            return suffix_array

        last_triple = len(text) - 3
        last_triple_index_in_T2 = (len(text) - 2) // 3 - 1
        position_to_insert = 0
        while (
            position_to_insert < len(suffix_array)
            and _compare_triples(text, suffix_array[position_to_insert], last_triple) < 0
        ):
            position_to_insert += 1

        if position_to_insert == 0:
            return [last_triple_index_in_T2] + suffix_array

        if position_to_insert == len(suffix_array):
            return suffix_array + [last_triple_index_in_T2]

        return suffix_array[:position_to_insert] + [last_triple_index_in_T2] + suffix_array[position_to_insert:]

    suffix_array_T2 = _sort_initial_suffix_array_T2_by_first_letter(initial_suffix_array_T2)

    return _add_last_triple(suffix_array_T2, text)


def _merge(text: List[int], suffix_array_T0_T1: List[int], suffix_array_T2: List[int]) -> List[int]:
    def _correct_indexes_from_T0_T1(suffix_array_T0_T1: List[int]) -> List[int]:
        mid = (len(suffix_array_T0_T1) - 1) // 2

        def _is_T0_index(index) -> bool:
            return index <= mid

        return list(
            map(
                lambda T0_T1_index: 3 * T0_T1_index if _is_T0_index(T0_T1_index) else (T0_T1_index - (mid + 1)) * 3 + 1,
                suffix_array_T0_T1,
            )
        )

    def _correct_indexes_from_T2(suffix_array_T2: List[int]) -> List[int]:
        return list(
            map(
                lambda T2_index: T2_index * 3 + 2,
                suffix_array_T2,
            ),
        )

    T0_T1 = _correct_indexes_from_T0_T1(suffix_array_T0_T1)
    T2 = _correct_indexes_from_T2(suffix_array_T2)

    T0_T1_pointer = 0
    T2_pointer = 0
    suffix_array = []
    while T0_T1_pointer < len(T0_T1) and T2_pointer < len(T2):
        if _compare_triples(text, T0_T1[T0_T1_pointer], T2[T2_pointer]) < 0:
            suffix_array.append(T0_T1[T0_T1_pointer])
            T0_T1_pointer += 1
        else:
            suffix_array.append(T2[T2_pointer])
            T2_pointer += 1

    while T0_T1_pointer < len(T0_T1):
        suffix_array.append(T0_T1[T0_T1_pointer])
        T0_T1_pointer += 1

    while T2_pointer < len(T2):
        suffix_array.append(T2[T2_pointer])
        T2_pointer += 1

    return suffix_array
