from os import linesep

import numpy as np


def parse(input: str):
    lines = input.split(linesep)

    paths = []

    for line in lines:
        points = line.split(" -> ")

        paths.append([tuple(int(x) for x in point.split(",")) for point in points])

    return paths


def generate_line(start: tuple[int, int], end: tuple[int, int]):
    if start[0] == end[0]:
        a, b = min(start[1], end[1]), max(start[1], end[1])
        return [(start[0], y) for y in range(a, b + 1)]
    if start[1] == end[1]:
        a, b = min(start[0], end[0]), max(start[0], end[0])
        return [(x, start[1]) for x in range(a, b + 1)]


def part_1(paths: list[list[tuple[int, int]]]):
    rocks = set()

    for path in paths:
        for i in range(1, len(path)):
            rocks.update(generate_line(path[i - 1], path[i]))

    collideable = set(rocks)

    falling_sand = None
    rest_amount = 0

    max_y = max(*(rock[1] for rock in rocks))

    while True:
        if falling_sand is None:
            falling_sand = [500, 0]

        if falling_sand[1] > max_y:
            break

        s = falling_sand

        if (s[0], s[1] + 1) not in collideable:
            s[1] += 1
        elif (s[0] - 1, s[1] + 1) not in collideable:
            s[0] -= 1
            s[1] += 1
        elif (s[0] + 1, s[1] + 1) not in collideable:
            s[0] += 1
            s[1] += 1
        else:
            # print("sand rest at", falling_sand)
            collideable.add(tuple(falling_sand))
            falling_sand = None
            rest_amount += 1

    return rest_amount


def part_2(paths: list[list[tuple[int, int]]]):
    rocks = set()

    for path in paths:
        for i in range(1, len(path)):
            rocks.update(generate_line(path[i - 1], path[i]))

    collideable = set(rocks)

    falling_sand = None
    rest_amount = 0

    max_y = max(*(rock[1] for rock in rocks)) + 2

    while True:
        if falling_sand is None:
            falling_sand = [500, 0]

        s = falling_sand

        if s[1] == max_y - 1:
            collideable.add(tuple(falling_sand))
            falling_sand = None
            rest_amount += 1
            continue

        if (s[0], s[1] + 1) not in collideable:
            s[1] += 1
        elif (s[0] - 1, s[1] + 1) not in collideable:
            s[0] -= 1
            s[1] += 1
        elif (s[0] + 1, s[1] + 1) not in collideable:
            s[0] += 1
            s[1] += 1
        else:
            rest_amount += 1
            collideable.add(tuple(falling_sand))
            falling_sand = None

            if s == [500, 0]:
                break

    return rest_amount
