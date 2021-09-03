class Node:
  def __init__(self, value):
    if value == None:
      raise ValueError('value is empty')

    self.value = value