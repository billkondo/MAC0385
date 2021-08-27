from persistent_deque.node import Node

class Deque:
  def __init__(self, first = None, last = None):
    if first != None and type(first) != Node:
      raise ValueError('first is not None neither Node')

    if last != None and type(last) != Node:
      raise ValueError('last is not None neither Node')

    if first == None and last != None:
      raise ValueError('first is None but last is not None')

    if first != None and last == None:
      raise ValueError('first is not None but last is None')

    self.first = first
    self.last = last