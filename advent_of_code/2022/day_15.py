import re
from time import time


def parse(input: str):
    "Sensor at x=3805407, y=3099635: closest beacon is at x=3744251, y=2600851"

    matches = re.findall(
        r"Sensor at x=(\d+), y=(\d+): closest beacon is at x=(\d+), y=(\d+)", input
    )

    closest_beacons = {}

    for match in matches:
        sx, sy, bx, by = map(int, match)

        closest_beacons[(sx, sy)] = (bx, by)

    return closest_beacons


def get_distance(a: tuple[int, int], b: tuple[int, int]):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def get_bounding_box(points: list[tuple[int, int]]):
    x = [p[0] for p in points]
    y = [p[1] for p in points]

    return ((min(*x), min(*y)), (max(*x), max(*y)))


def get_intersection_range(point: tuple[int, int], d: int, y: int):
    y_dist = abs(point[1] - y)

    if y_dist > d:
        return None

    offset = d - y_dist

    return (point[0] - offset, point[0] + offset)


def get_merged_length(ranges: list[tuple[int, int]]):
    ordered = sorted(ranges, key=lambda r: r[0])
    sum = 0
    x = ordered[0][0] - 1

    for r in ordered:
        a = max(x + 1, r[0])
        b = r[1]

        if a <= b:
            sum += b - a + 1
            x = b

    return sum


def part_1(closest_beacons: dict[tuple[int, int], tuple[int, int]]):
    distances = {
        sensor: get_distance(sensor, beacon)
        for sensor, beacon in closest_beacons.items()
    }

    beacons = set(closest_beacons.values())
    sensors = set(closest_beacons.keys())

    y = 2_000_000

    ranges = [
        r
        for point, d in distances.items()
        if (r := get_intersection_range(point, d, y)) is not None
    ]

    num = get_merged_length(ranges)
    num -= len([pos for pos in (*sensors, *beacons) if pos[1] == y])

    return num
