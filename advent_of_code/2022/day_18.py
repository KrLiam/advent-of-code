from os import linesep


def parse(input: str):
    lines = input.split(linesep)

    return set(tuple(int(x) for x in line.split(",")) for line in lines)


def get_adjacent(pos: tuple[int, int, int]):
    x, y, z = pos

    return [
        (x + 1, y, z),
        (x, y + 1, z),
        (x, y, z + 1),
        (x - 1, y, z),
        (x, y - 1, z),
        (x, y, z - 1),
    ]


def part_1(droplets: set[tuple[int, int, int]]):
    surface = 0

    for droplet in droplets:
        for adj in get_adjacent(droplet):
            if adj not in droplets:
                surface += 1

    return surface


def is_inside(
    pos: tuple[int, int, int],
    droplets: set[tuple[int, int, int]],
    boundary: tuple[tuple[int, int, int], tuple[int, int, int]],
    cache: dict[tuple[int, int, int], bool] = {},
):
    min, max = boundary

    checked = set()
    active = [pos]
    checked.add(pos)

    def store_cache(value: bool):
        for pos in checked:
            cache[pos] = value

        return value

    while active:
        current = active.pop(0)

        for adj in get_adjacent(current):
            if adj in cache:
                return store_cache(cache[adj])

            if (
                not (min[0] < adj[0] < max[0])
                or not (min[1] < adj[1] < max[1])
                or not (min[2] < adj[2] < max[2])
            ):
                return store_cache(False)

            if adj not in droplets and adj not in checked:
                checked.add(adj)
                active.append(adj)

    return store_cache(True)


def part_2(droplets: set[tuple[int, int, int]]):
    max_pos = tuple(max(p[i] for p in droplets) for i in range(3))
    min_pos = tuple(min(p[i] for p in droplets) for i in range(3))

    surface = 0

    for droplet in droplets:
        for adj in get_adjacent(droplet):
            if adj not in droplets and not is_inside(adj, droplets, (min_pos, max_pos)):
                surface += 1

    return surface
