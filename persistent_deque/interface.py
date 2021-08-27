from persistent_deque.node import AddLeaf, Depth\
  , LevelAncestor, LowestCommonAncestor
from persistent_deque.deque import Deque

def NewDeque() -> Deque:
  return Deque(None, None)

def Front(deque : Deque):
  return deque.first.value

def Back(deque : Deque):
  return deque.last.value

def PushFront(deque: Deque, value : int) -> Deque:
  if deque.first == None:
    root = AddLeaf(value, None)
    return Deque(root, root)
  else:
    return Deque(AddLeaf(value, deque.first), deque.last)

def Swap(deque:Deque) -> Deque:
  return Deque(deque.last, deque.first)

def PushBack(deque: Deque, value) -> Deque:
  return Swap(PushFront(Swap(deque), value))

def Kth(deque : Deque, k : int) -> Deque:
  u = deque.first
  v = deque.last

  mid = LowestCommonAncestor(u, v)

  path_length = Depth(u) + Depth(v) - 2 * Depth(mid)
  if k > path_length:
    raise ValueError('k is greater than path length')

  first_half_length = Depth(u) - Depth(mid)
  is_in_first_half = k <= first_half_length

  if is_in_first_half:
    return LevelAncestor(k, u)

  second_half_length = Depth(v) - Depth(mid)
  return LevelAncestor(second_half_length - (k - first_half_length), v)