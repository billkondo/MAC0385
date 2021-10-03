class Operation:
    def __init__(
        self,
        time=None,
        type=None,
        key=None,
    ):
        if not isinstance(time, int):
            raise TypeError("time is not a int")

        if not isinstance(type, int):
            raise TypeError("type is not a int")

        if type < -1 or type > 1:
            raise ValueError("type is not in range [-1, 1]")

        if key is not None and not isinstance(key, int):
            raise TypeError("key in not a int")

        if type != -1 and key is None:
            raise ValueError(
                "insert operation(type = 1 or type = 0) has empty key"
            )

        if type == -1 and key is not None:
            raise ValueError("delete operation(type = -1) has non-empty key")

        self.time: int = time
        self.key: int = key
        self.type: int = type
