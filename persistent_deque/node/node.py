class Node:
  def __init__(self, value, parent, depth, jump = None):
    if type(value) != int:
      raise TypeError('value is not an integer')

    if parent != None and type(parent) != Node:
      raise TypeError('parent is not None neither a Node')

    if type(depth) != int:
      raise TypeError('depth is not an integer')

    if depth < 0:
      raise ValueError('depth should not be less than zero')

    if jump != None and type(jump) != Node:
      raise TypeError('jump is not None neither a Node')

    self.value = value
    self.parent: Node or None = parent
    self.depth: int = depth
    self.jump: Node or Node = jump