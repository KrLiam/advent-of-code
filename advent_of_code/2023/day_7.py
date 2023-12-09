
from enum import Enum
from functools import cache
from typing import Literal


def parse(txt: str) -> tuple[list[str], dict[str, int]]:
    hands: list[str] = []
    bids: dict[str, int] = {}

    for line in txt.split("\n"):
        hand, bid = line.split(" ")

        hands.append(hand)
        bids[hand] = int(bid)
    
    return (hands, bids)


ORDER = {
    "A": 12,
    "K": 11,
    "Q": 10,
    "J": 9,
    "T": 8,
    "9": 7,
    "8": 6,
    "7": 5,
    "6": 4,
    "5": 3,
    "4": 2,
    "3": 1,
    "2": 0,
}


class HandKind:
    HighCard = 0
    OnePair = 1
    TwoPair = 2
    ThreeOfAKind = 3
    FullHouse = 4
    FourOfAKind = 5
    FiveOfAKind = 6


@cache
def get_type(hand: str) -> int:
    diff_cards = set(hand)
    count = tuple(hand.count(ch) for ch in diff_cards)

    diff = len(diff_cards)

    if diff == 1:
        return HandKind.FiveOfAKind
    if diff == 2 and 4 in count:
        return HandKind.FourOfAKind
    if diff == 2 and 3 in count:
        return HandKind.FullHouse
    if diff == 3 and 3 in count:
        return HandKind.ThreeOfAKind
    if diff == 3:
        return HandKind.TwoPair
    if diff == 4 and 2 in count:
        return HandKind.OnePair
    if diff == 5:
        return HandKind.HighCard
    
    raise ValueError("Fuck me.")

@cache
def get_order(hand: str):
    res = 0

    max_i = len(hand) - 1
    for i, ch in enumerate(hand):
        res |= ORDER[ch] << (max_i - i)*4

    return res


def part_1(hands: list[str], bids: dict[str, int]) -> int:
    hands = sorted(hands, key=lambda h: (get_type(h), get_order(h)))

    return sum(
        (rank + 1) * bids[hand] for rank, hand in enumerate(hands)
    )

def part_2(hands: list[str], bids: dict[str, int]) -> int:
    ...
