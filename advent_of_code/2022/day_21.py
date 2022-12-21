from operator import add, mul, sub, truediv
from os import linesep

from sympy import Symbol, solve

OPERATIONS = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": truediv,
}


def parse(input: set):
    lines = input.split(linesep)

    jobs = {}

    for line in lines:
        name, _, value = line.partition(":")

        value = value.strip()

        if value.isdigit():
            value = int(value)
        else:
            value = tuple(value.split(" "))

        jobs[name] = value

    return jobs


def evaluate(name: str, values: dict[str, int | Symbol | tuple[str, str, str]]):
    value = values[name]

    if isinstance(value, tuple):
        left, op, right = value

        operator = OPERATIONS.get(op)
        left = evaluate(left, values)
        right = evaluate(right, values)

        value = operator(left, right)

    return value


def part_1(jobs: dict[str, int | tuple[str, str, str]]):
    return int(evaluate("root", jobs))


def part_2(jobs: dict[str, int | tuple[str, str, str]]):
    jobs["humn"] = Symbol("x")

    left, _, right = jobs["root"]

    left = evaluate(left, jobs)
    right = evaluate(right, jobs)

    x, *_ = solve(left - right)

    return int(x)
