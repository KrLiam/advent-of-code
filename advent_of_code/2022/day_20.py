from os import linesep
from typing import Any


class Node:
    def __init__(self, value: Any):
        self.value = int(value)

    def __int__(self):
        return self.value

    def __repr__(self):
        return str(self.value)


def parse(input: str):
    return [Node(n) for n in input.split(linesep)]


def move(seq: list[Node], element: Node):
    i = seq.index(element)

    seq.pop(i)

    seq.insert((i + element.value) % len(seq), element)


def get_value(seq: list[Node], index: int):
    return seq[index % len(seq)].value


def part_1(sequence: list[Node]):
    result = list(sequence)

    for n in sequence:
        move(result, n)

    for zero_i, n in enumerate(result):
        if n.value == 0:
            break

    summed = (
        get_value(result, zero_i + 1000)
        + get_value(result, zero_i + 2000)
        + get_value(result, zero_i + 3000)
    )

    return summed


def part_2(sequence: list[Node]):
    result = list(sequence)

    for n in sequence:
        n.value *= 811589153

    for n in sequence * 10:
        move(result, n)

    for zero_i, n in enumerate(result):
        if n.value == 0:
            break

    summed = (
        get_value(result, zero_i + 1000)
        + get_value(result, zero_i + 2000)
        + get_value(result, zero_i + 3000)
    )

    return summed
