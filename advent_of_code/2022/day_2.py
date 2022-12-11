from os import linesep

SHAPES = ["A", "B", "C"]


def get_shape_offset(shape: str, offset: int):
    i = (SHAPES.index(shape) + offset) % len(SHAPES)

    return SHAPES[i]


def calculate_score(opponent_shape: str, response_shape: str):
    win_response = get_shape_offset(opponent_shape, 1)

    if response_shape == win_response:
        score = 6
    elif opponent_shape == response_shape:
        score = 3
    else:
        score = 0

    return score + SHAPES.index(response_shape) + 1


def parse(input: str):
    lines = input.split(linesep)

    return [line.split(" ") for line in lines]


def part_1(rounds: list[list[str]]):
    response_map = {"X": "A", "Y": "B", "Z": "C"}

    return sum(calculate_score(op, response_map.get(res)) for op, res in rounds)


def part_2(rounds: list[list[str]]):
    response_map = {"X": -1, "Y": 0, "Z": 1}

    return sum(
        calculate_score(op, get_shape_offset(op, response_map.get(res)))
        for op, res in rounds
    )
