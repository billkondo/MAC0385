class Operation:
    def __init__(self, key=None, type=None):
        if not isinstance(key, int):
            raise TypeError('key in not a int')

        if not isinstance(type, int):
            raise TypeError('type is not a int')

        if type < -1 or type > 1:
            raise TypeError('type is not in range [-1, 1]')

        self.key: int = key
        self.type: int = type
