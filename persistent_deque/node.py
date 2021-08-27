class Node:
  def __init__(self, value, parent, depth = 0):
    if type(value) != int:
      raise TypeError('value is not an integer')

    if parent != None and type(parent) != Node:
      raise TypeError('parent is not None neither a Node')

    if type(depth) != int:
      raise TypeError('depth is not an integer')

    if depth < 0:
      raise ValueError('depth should not be less than zero')

    self.value = value
    self.parent : Node or None = parent
    self.depth : int = depth