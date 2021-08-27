from persistent_deque.node import Node

def Depth(node: Node) -> int:
  # For root to have depth 0, None must have depth -1
  if node == None:
    return -1

  if type(node) != Node:
    raise TypeError('node is not a Node')

  return node.depth

def Jump(parent: Node) -> Node:
  if parent == None:
    return None

  if (parent.jump != None and 
      Depth(parent) - Depth(parent.jump) ==
      Depth(parent.jump) - Depth(parent.jump.jump)):  
    return parent.jump.jump

  return parent

def AddLeaf(value : int, parent: Node) -> Node:
  return Node(value, parent, Depth(parent) + 1, Jump(parent))
