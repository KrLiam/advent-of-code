from argparse import ArgumentParser

from advent_of_code import solve_puzzle, create_solution


def solve():
    parser = ArgumentParser()

    parser.add_argument("year", type=int)
    parser.add_argument("day", type=int)
    parser.add_argument("--part-2", action="store_true", default=False)

    args = parser.parse_args()

    solve_puzzle(args.year, args.day, args.part_2)


def create():
    parser = ArgumentParser()

    parser.add_argument("year", type=int)
    parser.add_argument("day", type=int)

    args = parser.parse_args()

    print(f"Creating solution for day {args.year}.{args.day}...")

    create_solution(args.year, args.day)

    print("Done!")
