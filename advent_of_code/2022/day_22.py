import re
from os import linesep

import numpy as np


def parse(input: str):
    map, instructions_str = input.split(linesep * 2)
    lines = map.split(linesep)

    walls = set()
    rows = []

    for i, line in enumerate(lines):
        start = None

        for j, ch in enumerate(line):
            if ch == " ":
                continue

            if start is None:
                start = j

            if ch == "#":
                walls.add((j, i))

        rows.append((start, j))

    columns = []
    num_columns = max(n for _, n in rows) + 1

    for j in range(num_columns):
        start = None
        end = None

        for i, (min, maxr) in enumerate(rows):
            if not (min <= j <= maxr):
                continue

            if start is None:
                start = i

            end = i

        columns.append((start, end))

    instructions = [
        int(match) if match.isdigit() else match
        for match in re.findall(r"(\d+|[LR])", instructions_str)
    ]

    return rows, columns, walls, instructions


def get_initial_pos(rows: list[tuple[int, int]], walls: set[tuple[int, int]]):
    min, max = rows[0]

    for j in range(min, max + 1):
        if (j, 0) not in walls:
            return np.array([j, 0])


DIRECTIONS = [
    np.array([1, 0]),
    np.array([0, 1]),
    np.array([-1, 0]),
    np.array([0, -1]),
]


def part_1(
    rows: list[tuple[int, int]],
    columns: list[tuple[int, int]],
    walls: set[tuple[int, int]],
    instructions: list[int | str],
):
    pos = get_initial_pos(rows, walls)

    direction = 0

    for move in instructions:
        if isinstance(move, int):
            movement = DIRECTIONS[direction]

            for _ in range(move):
                new_pos = pos + movement

                if movement[0]:
                    row_min, row_max = rows[new_pos[1]]
                    row_length = row_max - row_min + 1
                    new_pos[0] = (new_pos[0] - row_min) % row_length + row_min

                if movement[1]:
                    column_min, column_max = columns[new_pos[0]]
                    column_length = column_max - column_min + 1
                    new_pos[1] = (new_pos[1] - column_min) % column_length + column_min

                if tuple(new_pos) in walls:
                    break

                pos = new_pos
        else:
            direction += 1 if move == "R" else -1
            direction %= 4

    return 1000 * (pos[1] + 1) + 4 * (pos[0] + 1) + direction
