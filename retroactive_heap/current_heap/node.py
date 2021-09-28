class Node:
    def __init__(self, key=None, time=None):
        if not isinstance(key, int):
            raise TypeError("key is not a int")

        if not isinstance(time, int):
            raise TypeError("time is not a int")

        self.key: int = key
        self.time: int = time
