from persistent_deque.node import Node

def node_function_wrapper(function):
  def wrapper(node: Node):
    if node == None:
      raise ValueError('node is None')
  
    if type(node) != Node:
      raise TypeError('node is not a Node')

    return function(node)
  
  return wrapper

@node_function_wrapper
def Depth(node: Node):
  return node.depth

def AddLeaf(value : int, parent: Node) -> Node:
  return Node(value, parent, parent.depth + 1)