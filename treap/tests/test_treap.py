import random
import unittest

from treap import Treap, TreapNode


class TestTreap(unittest.TestCase):
    def __is_heap__(self, root: TreapNode):
        if root is None:
            return

        if not root.is_heap:
            raise RuntimeError("not a heap")

        self.__is_heap__(root.L)
        self.__is_heap__(root.R)

    def __is_bst__(self, root: TreapNode):
        if root is None:
            return

        if root.L is not None and root.L.key > root.key:
            raise RuntimeError("not a bst")

        if root.R is not None and root.R.key < root.key:
            raise RuntimeError("not a bst")

        self.__is_bst__(root.L)
        self.__is_bst__(root.R)

    def __is_treap__(self, treap: Treap):
        self.__is_bst__(treap.__root__)
        self.__is_heap__(treap.__root__)

    def __insert__(self, treap: Treap, key: int):
        treap.insert(key)
        self.__is_treap__(treap)

    def __insert_even__(self, treap: Treap):
        for key in range(0, 100, 2):
            self.__insert__(treap, key)

    def __insert_odd__(self, treap: Treap):
        for key in range(1, 100, 2):
            self.__insert__(treap, key)

    def __assert_search__(self, treap: Treap):
        for key in range(0, 100):
            self.assertTrue(treap.search(key))

        self.assertFalse(treap.search(-1))
        self.assertFalse(treap.search(100))

    def __delete__(self, treap: Treap, key: int):
        self.assertTrue(treap.search(key))
        treap.delete(key)
        self.assertFalse(treap.search(key))
        self.__is_treap__(treap)

    def __delete_multiple_of_3__(self, treap: Treap):
        for key in range(0, 100, 3):
            self.__delete__(treap, key)

    def test_treap(self):
        random.seed(123)
        treap = Treap()
        self.__insert_even__(treap)
        self.__insert_odd__(treap)
        self.__assert_search__(treap)
        self.__delete_multiple_of_3__(treap)
        self.assertEqual(treap.min(), 1)
