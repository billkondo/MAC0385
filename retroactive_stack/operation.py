from typing import Any

class Operation:
  def __init__(self, type = None, value = None):
    if type != -1 and type != 1:
      raise ValueError('type is not -1 neither 1')

    if type == -1 and value != None:
      raise ValueError('type is -1, but value is not None')

    if type == 1 and value == None:
      raise ValueError('type is 1, but value is None')

    self.type: int = type
    self.value: Any = value