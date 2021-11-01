import unittest

from splay_tree import SplayTree, SplayTreeNode


class TestSplayTree(unittest.TestCase):
    def __is_bst__(self, root: SplayTreeNode):
        if root is None:
            return

        if root.L is not None and root.L.key > root.key:
            raise RuntimeError("not a bst")

        if root.R is not None and root.R.key < root.key:
            raise RuntimeError("not a bst")

        self.__is_bst__(root.L)
        self.__is_bst__(root.R)

    def __is_splay_tree__(self, splay_tree: SplayTree):
        self.__is_bst__(splay_tree.__root__)

    def __insert__(self, splay_tree: SplayTree, key: int):
        splay_tree.insert(key)
        self.__is_splay_tree__(splay_tree)
        self.assertEqual(splay_tree.__root__.key, key)

    def __insert_even__(self, splay_tree: SplayTree):
        for key in range(0, 100, 2):
            self.__insert__(splay_tree, key)

    def __insert_odd__(self, splay_tree: SplayTree):
        for key in range(1, 100, 2):
            self.__insert__(splay_tree, key)

    def __delete__(self, splay_tree: SplayTree, key: int):
        self.assertTrue(splay_tree.search(key))
        splay_tree.delete(key)
        self.assertFalse(splay_tree.search(key))
        self.__is_splay_tree__(splay_tree)

    def __delete_multiple_of_3__(self, splay_tree: SplayTree):
        for key in range(0, 100, 3):
            self.__delete__(splay_tree, key)

    def __assert_search__(self, splay_tree: SplayTree):
        self.assertFalse(splay_tree.search(-1))
        self.assertFalse(splay_tree.search(100))

        for key in range(0, 100):
            self.assertTrue(splay_tree.search(key))

    def __delete_all__(self, splay_tree: SplayTree):
        for key in range(0, 100):
            if splay_tree.search(key):
                self.__delete__(splay_tree, key)

    def test_splay_tree(self):
        splay_tree = SplayTree()
        self.__insert_even__(splay_tree)
        self.__insert_odd__(splay_tree)
        self.__assert_search__(splay_tree)
        self.__delete_multiple_of_3__(splay_tree)
        self.assertEqual(splay_tree.min(), 1)
        self.__delete_all__(splay_tree)

        self.__insert_even__(splay_tree)
        self.__insert_odd__(splay_tree)
        self.__assert_search__(splay_tree)
