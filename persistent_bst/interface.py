from persistent_bst.bst import BST
from persistent_bst.node.interface import CopyNode, InsertNode, SearchNode

def NewBST() -> BST:
  return BST()

def CopyBST(b: BST) -> BST:
  if b == None:
    raise ValueError('b is None')

  root_copy = CopyNode(b.root)
  return BST(root_copy)

def Insert(b: BST, value) -> BST:
  if b == None:
    raise ValueError('b is None')

  if type(b) != BST:
    raise TypeError('b is not a BST')

  return BST(InsertNode(b.root, value))

def Search(b: BST, value) -> bool:
  if b == None:
    raise ValueError('b is None')

  if type(b) != BST:
    raise TypeError('b is not a BST')

  return SearchNode(b.root, value)