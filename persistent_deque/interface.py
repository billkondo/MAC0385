from typing import Deque

from persistent_deque.deque import Deque

def NewDeque():
  return Deque(None, None)

def Front(deque : Deque):
  return deque.first.value

def Back(deque : Deque):
  return deque.last.value