from argparse import ArgumentParser

from advent_of_code import solve_puzzle


def solve():
    parser = ArgumentParser()

    parser.add_argument("year", type=int)
    parser.add_argument("day", type=int)
    parser.add_argument("--part-2", action="store_true", default=False)

    args = parser.parse_args()

    solve_puzzle(args.year, args.day, args.part_2)
