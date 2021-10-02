from avl.avl_node import AVLNode


def Insert(node: AVLNode, newNode: AVLNode) -> AVLNode:
    if not isinstance(newNode, AVLNode):
        raise TypeError("newNode is not a AVLNode")

    if node is None:
        return newNode

    if not isinstance(node, AVLNode):
        raise TypeError("node is not a AVLNode")

    if newNode.key <= node.key:
        node.L = Insert(node.L, newNode)
    else:
        node.R = Insert(node.R, newNode)

    node.update()
    return Balance(node)


def Delete(node: AVLNode, key: int) -> AVLNode:
    if not isinstance(node, AVLNode):
        raise TypeError("node is not a AVLNode")

    if node.key == key:
        if node.R is not None:
            min_node = Min(node.R)
            min_node.R = Delete(node.R, min_node.key)
            min_node.L = node.L
            min_node.update()
            return Balance(min_node)

        if node.L is not None:
            return node.L

        return None

    if key < node.key:
        node.L = Delete(node.L, key)
    else:
        node.R = Delete(node.R, key)

    node.update()
    return Balance(node)


def Find(node: AVLNode, key: int) -> AVLNode:
    if node is None:
        return None

    if not isinstance(node, AVLNode):
        raise TypeError("node is not a AVLNode")

    if node.key == key:
        return node

    if node.L is not None and key < node.key:
        return Find(node.L, key)

    if node.R is not None and node.key < key:
        return Find(node.R, key)

    return None


def Min(node: AVLNode) -> AVLNode:
    if not isinstance(node, AVLNode):
        raise TypeError("node is not a AVLNode")

    if node.L is not None:
        return Min(node.L)

    return node


def RotateRight(node: AVLNode) -> AVLNode:
    #          x             y
    #        / |           / |
    #       y  T3   =>   T1  x
    #     / |              / |
    #   T1  T2           T2  T3

    if not isinstance(node, AVLNode):
        raise TypeError("node is not a AVLNode")

    if node.L is None:
        return node

    x = node
    y = node.L
    t2 = y.R

    y.R = x
    x.L = t2

    x.update()
    y.update()

    return y


def RotateLeft(node: AVLNode) -> AVLNode:
    #          y               x
    #        / |             / |
    #      T1  x   =>       y  T3
    #        / |          / |
    #      T2  T3       T1  T2

    if not isinstance(node, AVLNode):
        raise TypeError("node is not a AVLNode")

    if node.R is None:
        return node

    y = node
    x = node.R
    t2 = x.L

    y.R = t2
    x.L = y

    y.update()
    x.update()

    return x


def Balance(node: AVLNode) -> AVLNode:
    if not isinstance(node, AVLNode):
        raise TypeError("node is not a AVLNode")

    if node.balance <= -2:
        if node.L is not None and node.L.balance <= 0:
            return RotateRight(node)

        node.L = RotateLeft(node.L)
        return RotateRight(node)

    if node.balance >= 2:
        if node.R is not None and node.R.balance >= 0:
            return RotateLeft(node)

        node.R = RotateRight(node.R)
        return RotateLeft(node)

    return node
