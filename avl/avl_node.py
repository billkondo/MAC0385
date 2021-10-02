class AVLNode:
    def __init__(self, key=None):
        if not isinstance(key, int):
            raise TypeError("key is not a int")

        self.key: int = key

        self.height: int = 0
        self.balance: int = 0
