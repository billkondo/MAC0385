from persistent_deque.node import Node
from persistent_deque.deque import Deque

def NewDeque() -> Deque:
  return Deque(None, None)

def Front(deque : Deque):
  return deque.first.value

def Back(deque : Deque):
  return deque.last.value

def PushFront(deque: Deque, value) -> Deque:
  if deque.first == None:
    root = Node(value, None, 0)
    return Deque(root, root)
  else:
    return Deque(Node(value, deque.first, deque.first.depth + 1), deque.last)