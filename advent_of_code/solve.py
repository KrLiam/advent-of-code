from importlib import import_module
from time import time

from .download import load_input


def solve_puzzle(year: int, day: int, part_two: bool = False):
    input = load_input(year, day)

    module = import_module(f"advent_of_code.{year}.day_{day}")

    parse = getattr(module, "parse", None)

    start_time = time()

    if parse:
        input = parse(input)

    name = "part_2" if part_two else f"part_1"
    solve = getattr(module, name)

    if isinstance(input, tuple):
        answer = solve(*input)
    else:
        answer = solve(input)

    end_time = time()

    print(
        f"The answer is {answer}",
        f"Took {(end_time - start_time)*1000:.0f}ms.",
        sep="\n",
    )
