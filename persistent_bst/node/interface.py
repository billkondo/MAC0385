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

def MinNode(node: Node) -> Node:
  if node == None:
    raise ValueError('node is None')

  if type(node) != Node:
    raise TypeError('node is not a Node')

  if node.left != None:
    return MinNode(node.left)

  return node

def SearchNode(node: Node, value) -> bool:
  if node != None and type(node) != Node:
    raise TypeError('node is not a Node')

  if value == None:
    raise ValueError('value is None')

  if node == None:
    return False

  if node.value == value:
    return True

  if value < node.value:
    return SearchNode(node.left, value)

  return SearchNode(node.right, value)

def DeleteNode(node: Node, value) -> Node:
  if node == None:
    raise ValueError('node is None')

  if type(node) != Node:
    raise TypeError('node is not a Node')

  if value == None:
    raise ValueError('value is None')

  if value == node.value:
    if node.right != None:
      min_node = MinNode(node.right)
      node_copy = CopyNode(min_node)
      node_copy.right = DeleteNode(node.right, min_node.value)
      node_copy.left = node.left
      return node_copy

    if node.left != None:
      return node.left

    return None

  node_copy = CopyNode(node)

  if value < node.value:
    node_copy.left = DeleteNode(node.left, value)

  if node.value < value:
    node_copy.right = DeleteNode(node.right, value)

  return node_copy

def PrintNode(node: Node) -> str:
  if node == None:
    return ""

  def print_in_order_traversal(u: Node, values):
    if u == None:
      return

    values.append(str(u.value))

    print_in_order_traversal(u.left, values)
    print_in_order_traversal(u.right, values)
      
  values = []
  print_in_order_traversal(node, values)

  return ' '.join(values)