from persistent_deque.node import Node

def Depth(node: Node):
  if node == None:
    raise ValueError('node is None')
  
  if type(node) != Node:
    raise TypeError('node is not a Node')

  return node.depth
