from functools import cache
from math import floor
import re
from typing import NamedTuple


class Card(NamedTuple):
    id: int
    winning: frozenset[int]
    nums: frozenset[int]


def parse(txt: str) -> list[Card]:
    cards = []

    for line in txt.split("\n"):
        left, right = line.split(" | ")

        prefix, winning_nums = left.split(":")

        normalized_prefix = " ".join(prefix.split())
        _, card = normalized_prefix.split(" ")

        normalized_winning_nums = " ".join(winning_nums.split())
        normalized_right = " ".join(right.split())
        winning = frozenset(int(n) for n in normalized_winning_nums.split(" "))
        nums = frozenset(int(n) for n in normalized_right.split(" "))

        cards.append(Card(int(card), winning, nums))

    return cards


def part_1(cards: list[Card]) -> int:
    result = 0

    for card in cards:
        matched = len(card.winning & card.nums)
        points = floor(2 ** (matched - 1))
        result += points

    return result


def part_2(cards: list[Card]) -> int:
    wins: dict[int, int] = {}

    for card in cards:
        matched = len(card.winning & card.nums)
        wins[card.id] = matched

    @cache
    def scratch(card: int):
        scratches = 1

        for card_i in range(card + 1, card + wins[card] + 1):
            scratches += scratch(card_i)

        return scratches

    return sum(scratch(card.id) for card in cards)
