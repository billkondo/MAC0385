from persistent_deque.node import Node

def Depth(node: Node) -> int:
  # For root to have depth 0, None must have depth -1
  if node == None:
    return -1

  if type(node) != Node:
    raise TypeError('node is not a Node')

  return node.depth

def AddLeaf(value : int, parent: Node) -> Node:
  return Node(value, parent, Depth(parent) + 1)