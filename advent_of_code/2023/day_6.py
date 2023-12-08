from math import ceil, floor, prod, sqrt


def parse(txt: str) -> tuple[list[int], list[int]]:
    time_str, dist_str = txt.split("\n")

    _, time_str = time_str.split(":")
    _, dist_str = dist_str.split(":")

    time = [int(n) for n in time_str.split()]
    dist = [int(n) for n in dist_str.split()]

    return (time, dist)


def part_1(time: list[int], dist: list[int]) -> int:
    result = []

    for t, d in zip(time, dist):
        # x * (t - x) - d
        # -x² + tx - d = 0

        sqrt_delta = sqrt(t**2 - 4 * d)

        left = (t - sqrt_delta) / 2
        right = (t + sqrt_delta) / 2

        round_left = ceil(left) if left % 1 else left + 1
        round_right = floor(right) if right % 1 else right - 1

        ways = round_right - round_left + 1
        result.append(ways)

    return prod(result)


def part_2(time: list[int], dist: list[int]) -> int:
    t = int("".join(str(n) for n in time))
    d = int("".join(str(n) for n in dist))

    # x * (t - x) - d
    # -x² + tx - d = 0

    sqrt_delta = sqrt(t**2 - 4 * d)

    left = (t - sqrt_delta) / 2
    right = (t + sqrt_delta) / 2

    round_left = ceil(left) if left % 1 else left + 1
    round_right = floor(right) if right % 1 else right - 1

    return round_right - round_left + 1
