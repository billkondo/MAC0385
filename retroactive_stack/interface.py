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


@stack_validator
def Delete(stack: Stack, time: int):
    stack.bst.delete(time)


@stack_validator
def Kth(stack: Stack, time: int, k: int) -> Any:
    return stack.bst.kth(
        key=time,
        k=k,
    )


@stack_validator
def Top(stack: Stack, time: int) -> Any:
    return stack.bst.kth(
        key=time,
        k=1,
    )
