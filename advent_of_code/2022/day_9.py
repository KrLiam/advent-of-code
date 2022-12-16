from os import linesep

import numpy as np


def parse(input: str):
    lines = input.split(linesep)
    result = []

    for l in lines:
        direction, steps = l.split(" ")
        result.append((direction, int(steps)))

    return result


DIRECTIONS = {
    "U": np.array([0, 1]),
    "R": np.array([1, 0]),
    "D": np.array([0, -1]),
    "L": np.array([-1, 0]),
}


def compute_knot(parent: np.array, child: np.array):
    diff = parent - child

    if any(abs(diff) > 1):
        step = np.sign(diff)
        child += step


def part_1(motions: list[tuple[str, int]]):
    head = np.array([0, 0])
    tail = np.array([0, 0])

    visited = {(0, 0)}

    for direction, steps in motions:
        for _ in range(steps):
            head += DIRECTIONS[direction]

            compute_knot(head, tail)

            visited.add(tuple(tail))

    return len(visited)


def part_2(motions: list[tuple[str, int]]):
    knots = [np.array([0, 0]) for _ in range(10)]

    visited = {(0, 0)}

    for direction, steps in motions:
        for _ in range(steps):
            knots[0] += DIRECTIONS[direction]

            for parent, child in zip(knots, knots[1:]):
                compute_knot(parent, child)

            visited.add(tuple(knots[-1]))

    return len(visited)
