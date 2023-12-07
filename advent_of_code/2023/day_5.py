from bisect import bisect
from dataclasses import dataclass
from typing import Any, Iterable, NamedTuple, Union


class Range(NamedTuple):
    start: int
    end: int

    def __contains__(self, value: int):
        if not isinstance(value, int):
            return False

        return self.start <= value < self.end

    def __and__(self, other: "Range") -> "Range":
        if not isinstance(other, Range):
            return other & self

        if self.end <= other.start:
            return Range(0, 0)

        return Range(max(self.start, other.start), min(self.end, other.end))

    def shift(self, value: int):
        return Range(self.start + value, self.end + value)

    def __sub__(self, other: Union["Range", "CompoundRange"]) -> "CompoundRange":
        if not self & other:
            return CompoundRange((self,))

        if isinstance(other, CompoundRange):
            result = CompoundRange((self,))
            for rang in other.ranges:
                result -= rang
            return result

        return CompoundRange(
            (Range(self.start, other.start), Range(other.end, self.end))
        )

    def __bool__(self):
        return self.start < self.end


@dataclass(init=False, eq=False, order=False)
class CompoundRange:
    ranges: tuple[Range]

    def __init__(self, ranges: Iterable[Union[Range, "CompoundRange"]]):
        flatten = []
        for r in ranges:
            if isinstance(r, CompoundRange):
                flatten.extend(r.ranges)
            else:
                flatten.append(r)

        self.ranges = tuple(r for r in flatten if r)

    def __contains__(self, value: int):
        return any(value in rang for rang in self.ranges)

    def __and__(self, value: Range) -> "CompoundRange":
        return CompoundRange(value & rang for rang in self.ranges)

    def __sub__(self, value: Union[Range, "CompoundRange"]) -> "CompoundRange":
        return CompoundRange(rang - value for rang in self.ranges)

    def __bool__(self):
        return any(self.ranges)


@dataclass
class Map:
    ranges: list[Range]
    shift: list[int]

    def map(self, value: Range) -> list[Range]:
        mapped = [(i, r) for i, rang in enumerate(self.ranges) if (r := value & rang)]
        unmapped = value - CompoundRange(pair[1] for pair in mapped)

        result = [r.shift(self.shift[i]) for i, r in mapped]
        result.extend(unmapped.ranges)

        return result


@dataclass
class Almanac:
    seeds: list[int]
    maps: list[Map]


def parse(txt: str) -> Almanac:
    seeds_str, *str_maps = txt.split("\n\n")

    _, seeds_str = seeds_str.split(":")
    seeds = [int(x) for x in seeds_str.strip().split(" ")]

    maps: list[list[Range]] = []

    for map_str in str_maps:
        ranges = []
        shift = []

        for line in map_str.split("\n")[1:]:
            dest_start, origin_start, length = [int(x) for x in line.strip().split(" ")]
            ranges.append(Range(origin_start, origin_start + length))
            shift.append(dest_start - origin_start)

        maps.append(Map(ranges, shift))

    return Almanac(seeds, maps)


def part_1(almanac: Almanac) -> int:
    seeds = [Range(seed, seed + 1) for seed in almanac.seeds]

    for num_map in almanac.maps:
        seeds = [rang for seed in seeds for rang in num_map.map(seed)]

    return min(seeds).start


def part_2(almanac: Almanac) -> int:
    seeds = [
        Range(almanac.seeds[i], almanac.seeds[i] + almanac.seeds[i + 1])
        for i in range(0, len(almanac.seeds), 2)
    ]

    for num_map in almanac.maps:
        seeds = [rang for seed in seeds for rang in num_map.map(seed)]

    return min(seeds).start
