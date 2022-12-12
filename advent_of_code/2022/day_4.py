from os import linesep


def parse(input: str):
    lines = input.split(linesep)

    return [
        tuple(tuple(int(n) for n in r.split("-")) for r in line.split(","))
        for line in lines
    ]


def part_1(pairs: list[tuple[tuple[int, int], tuple[int, int]]]):
    count = 0

    for range_a, range_b in pairs:
        if (
            range_a[0] <= range_b[0]
            and range_b[1] <= range_a[1]
            or range_b[0] <= range_a[0]
            and range_a[1] <= range_b[1]
        ):
            count += 1

    return count


def part_2(pairs: list[tuple[tuple[int, int], tuple[int, int]]]):
    count = 0

    for range_a, range_b in pairs:
        max_left = max(range_a[0], range_b[0])
        min_right = min(range_a[1], range_b[1])

        if max_left <= min_right:
            count += 1

    return count
