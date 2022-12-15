import re
from collections import namedtuple
from os import linesep
from typing import List

Step = namedtuple("Step", ("amount", "origin", "dest"))


def parse(input: str):
    crates_str, steps_str = input.split(linesep * 2, 1)

    crates_lines = crates_str.split(linesep)

    stacks = []

    for i in range(0, len(crates_lines[0]), 4):
        raw_stack = [line[i : i + 4] for line in crates_lines]
        stack = [s[1] for s in raw_stack[::-1] if s[1].isalpha()]

        stacks.append(stack)

    matched_steps = re.findall("move (\d+) from (\d+) to (\d+)", steps_str)
    steps = [Step(*map(int, step)) for step in matched_steps]

    return stacks, steps


def part_1(stacks: List[List[str]], steps: List[Step]):
    for step in steps:
        n = step.amount

        while n > 0:
            crate = stacks[step.origin - 1].pop()
            stacks[step.dest - 1].append(crate)

            n -= 1

    return "".join(stack[-1] for stack in stacks)


def part_2(stacks: List[List[str]], steps: List[Step]):
    for step in steps:
        origin_stack = stacks[step.origin - 1]

        i = len(origin_stack) - step.amount

        crates = origin_stack[i:]
        del origin_stack[i:]

        stacks[step.dest - 1].extend(crates)

    return "".join(stack[-1] for stack in stacks)
