from importlib import import_module

from .download import load_input


def solve_puzzle(year: int, day: int, part_two: bool = False):
    input = load_input(year, day)

    module = import_module(f"advent_of_code.{year}.day_{day}")

    parse = getattr(module, "parse", None)

    if parse:
        input = parse(input)

    name = "part_2" if part_two else f"part_1"
    solve = getattr(module, name)

    answer = solve(input)

    print(f"The answer is {answer}")
