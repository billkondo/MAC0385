from persistent_deque.node.node import Node


def Jump(parent: Node) -> Node:
    if parent is None:
        return None

    if (
        parent.depth - parent.jump.depth
        == parent.jump.depth - parent.jump.jump.depth
    ):
        return parent.jump.jump

    return parent


def AddLeaf(value: int, parent: Node) -> Node:
    return Node(
        value, parent, 0 if parent is None else parent.depth + 1, Jump(parent)
    )


def LevelAncestor(k: int, node: Node) -> Node:
    if type(k) != int:
        raise TypeError("k is not an integer")

    if node is None or type(node) != Node:
        raise TypeError("node is not a Node")

    if k > node.depth:
        raise ValueError("k is greater than node depth")

    target_depth = node.depth - k

    while node.depth != target_depth:
        if node.jump.depth >= target_depth:
            node = node.jump
        else:
            node = node.parent

    return node


def LowestCommonAncestor(u: Node, v: Node) -> Node:
    if u is None or type(u) != Node:
        raise TypeError("u is not a Node")

    if v is None or type(v) != Node:
        raise TypeError("v is not a Node")

    if u.depth > v.depth:
        u, v = v, u

    v = LevelAncestor(v.depth - u.depth, v)

    if v == u:
        return u

    while u.parent != v.parent:
        if u.jump != v.jump:
            u = u.jump
            v = v.jump
        else:
            u = u.parent
            v = v.parent

    return u.parent
