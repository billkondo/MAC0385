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

def LevelAncestor(k : int, node: Node) -> Node:
  if type(k) != int:
    raise TypeError('k is not an integer')

  if node == None:
    raise ValueError('node is None')

  if type(node) != Node:
    raise TypeError('node is not a Node')

  if k > Depth(node):
    raise ValueError('k is greater than node depth')

  target_depth = Depth(node) - k

  while Depth(node) != target_depth:
    if Depth(node.jump) >= target_depth:
      node = node.jump
    else:
      node = node.parent
  
  return node
