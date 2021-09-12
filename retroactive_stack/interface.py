from typing import Any

from retroactive_stack.operation import Operation
from retroactive_stack.stack import Stack


def stack_validator(function):
    def wrapper(*args):
        stack = args[0]
        time = args[1]

        if type(stack) is not Stack:
            raise TypeError("deque is not a Stack")

        if type(time) is not int:
            raise TypeError("time is not a int")

        return function(*args)

    return wrapper


def NewStack(bst=None) -> Stack:
    return Stack(bst)


@stack_validator
def AddPush(stack: Stack, time: int, value: Any):
    stack.bst.insert(
        key=time,
        operation=Operation(
            type=1,
            value=value,
        ),
    )


@stack_validator
def AddPop(stack: Stack, time: int):
    stack.bst.insert(
        key=time,
        operation=Operation(
            type=-1,
        ),
    )
