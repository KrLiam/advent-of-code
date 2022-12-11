from os import linesep


def get_priority(letter: str) -> int:
    ofsset = 96 if letter.islower() else 38

    return ord(letter) - ofsset


def parse(input: str):
    return input.split(linesep)


def part_1(rucksacks: list[str]):
    total = 0

    for items in rucksacks:
        i = len(items) // 2
        first, second = items[:i], items[i:]

        item, *_ = set(first).intersection(second)

        total += get_priority(item)

    return total


def part_2(rucksacks: list[str]):
    total = 0

    for i in range(0, len(rucksacks), 3):
        a, b, c = rucksacks[i : i + 3]

        badge, *_ = set(a).intersection(b, c)

        total += get_priority(badge)

    return total
