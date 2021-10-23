from dataclasses import dataclass


@dataclass(order=True)
class Certificate:
    expiration_time: int
    index: int
