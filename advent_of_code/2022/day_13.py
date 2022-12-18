import json
from functools import cmp_to_key
from os import linesep


def parse(input: str):
    pairs = input.split(linesep * 2)

    return [tuple(json.loads(x) for x in pair.split(linesep)) for pair in pairs]


def compare(left, right):
    match (left, right):
        case [int(), list()]:
            return compare([left], right)

        case [list(), int()]:
            return compare(left, [right])

        case [list(), list()]:
            for a, b in zip(left, right):
                res = compare(a, b)

                if res != 0:
                    return res

            return len(left) - len(right)

        case [int(), int()]:
            return left - right

    return 0


def part_1(pairs):
    count = 0

    for i, (left, right) in enumerate(pairs):
        if compare(left, right) < 0:
            count += i + 1

    return count


def part_2(pairs: list):
    key_a = [[2]]
    key_b = [[6]]

    packets = [*(packet for pair in pairs for packet in pair), key_a, key_b]

    packets = sorted(packets, key=cmp_to_key(compare))

    return (packets.index(key_a) + 1) * (packets.index(key_b) + 1)
