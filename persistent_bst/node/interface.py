from persistent_bst.node.node import Node

def CopyNode(node: Node) -> Node:
  if type(node) != Node:
    raise TypeError('node is not a Node')

  copy_node = Node(node.value)
  copy_node.left = node.left
  copy_node.right = node.right

  return copy_node

def InsertNode(node: Node, value):
  if node != None and type(node) != Node:
    raise TypeError('node is not a Node')

  if value == None:
    raise ValueError('value is None')

  if node == None:
    return Node(value)

  node_copy = CopyNode(node)

  if value <= node.value:
    node_copy.left = InsertNode(node.left, value)
  else:
    node_copy.right = InsertNode(node.right, value)

  return node_copy