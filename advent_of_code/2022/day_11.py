import re
from dataclasses import dataclass
from math import floor
from operator import add, mul
from os import linesep

monkey_pattern = re.compile(
    linesep.join(
        (
            r"Monkey (\d+):",
            r"  Starting items: ((?:\d+(?:, )?)+)",
            r"  Operation: new = (.+)",
            r"  Test: divisible by (\d+)",
            r"    If true: throw to monkey (\d+)",
            r"    If false: throw to monkey (\d+)",
        )
    )
)


@dataclass
class Monkey:
    num: int
    items: list[int]
    op: tuple[str, str, str]
    test: int
    on_true: int
    on_false: int

    inspections: int = 0

    operators = {"+": add, "*": mul}

    def operate(self, item: int):
        _, op, a = self.op

        op = self.operators[op]

        return op(item, int(a)) if a.isdigit() else op(item, item)

    def round(self, relief=True):
        # print(f"\nMonkey {self.num}:")

        while self.items:
            item = self.items.pop(0)
            # print(f"    Inspects item of level {item}")

            item = self.operate(item)

            # print(f"        Item operated to {item}")

            if relief:
                item = floor(item / 3)

            # print(f"        Got bored, {item}")

            if item % self.test == 0:
                receiver_num = self.on_true
            else:
                receiver_num = self.on_false

            self.inspections += 1

            # print(f"        Item {item} is thrown to monkey {receiver_num}")

            yield receiver_num, item

    def receive_item(self, item: int):
        self.items.append(item)


def parse(input: str):
    matches = monkey_pattern.findall(input)

    return {
        int(num): Monkey(
            num=int(num),
            items=[int(n) for n in items.split(", ")],
            op=tuple(op.split(" ")),
            test=int(test),
            on_true=int(on_true),
            on_false=int(on_false),
        )
        for num, items, op, test, on_true, on_false in matches
    }


def get_business_level(monkeys: dict[int, Monkey]):
    inspections = sorted(monkeys.values(), key=lambda m: m.inspections)

    *_, a, b = inspections

    return a.inspections * b.inspections


def part_1(monkeys: dict[int, Monkey]):
    for _ in range(20):
        for monkey in monkeys.values():
            for receiver_id, item in monkey.round():
                monkeys[receiver_id].receive_item(item)

    return get_business_level(monkeys)


def part_2(monkeys: dict[int, Monkey]):
    mod = 1
    for monkey in monkeys.values():
        mod *= monkey.test

    for _ in range(10_000):
        for monkey in monkeys.values():
            for receiver_id, item in monkey.round(relief=False):
                item %= mod

                monkeys[receiver_id].receive_item(item)

    return get_business_level(monkeys)
