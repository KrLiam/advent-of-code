import re


def parse(input: str) -> list[str]:
    return input.split("\n")


def part_1(document: list[str]):
    sum = 0

    for line in document:
        digits = re.findall(r"\d", line)
        sum += int(digits[0] + digits[-1])

    return sum


DIGITS = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def part_2(document: list[str]):
    pattern = rf"(?=(\d|{'|'.join(DIGITS.keys())}))"

    sum = 0
    for line in document:
        digits = re.findall(pattern, line)
        first, last = digits[0], digits[-1]
        sum += int(DIGITS.get(first, first) + DIGITS.get(last, last))

    return sum
