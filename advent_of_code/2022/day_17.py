def parse(input: str):
    return list(input)


ROCKS = [
    [(0, 0), (1, 0), (2, 0), (3, 0)],
    [(1, 0), (0, 1), (1, 1), (2, 1), (1, 2)],
    [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)],
    [(0, 0), (0, 1), (0, 2), (0, 3)],
    [(0, 0), (1, 0), (0, 1), (1, 1)],
]


def create_rock(i: int, pos: tuple[int, int]):
    pattern = ROCKS[i]
    px, py = pos

    return [(x + px, y + py) for x, y in pattern]


def move_rock(rock: list[tuple[int, int]], delta: tuple[int, int]):
    dx, dy = delta

    return [(x + dx, y + dy) for x, y in rock]


def get_min(rock: list[tuple[int, int]], i: int):
    return min(*(pos[i] for pos in rock))


def get_max(rock: list[tuple[int, int]], i: int):
    return max(*(pos[i] for pos in rock))


def print_rocks(rocks: set[tuple[int, int]]):
    highest_y = get_max(rocks, 1)

    for y in range(highest_y, 0, -1):
        line = ""

        for x in range(0, 7):
            line += "#" if (x, y) in rocks else "."

        print(line)


def part_1(jets: list[str]):
    rocks = set()
    rock_i = 0
    jet_i = 0
    jet_amt = len(jets)

    active_rock = None
    highest_y = 0
    rock_count = 0

    while rock_count < 2022:
        if active_rock is None:
            active_rock = create_rock(rock_i % 5, (2, highest_y + 4))
            rock_i += 1

        movement = (1, 0) if jets[jet_i % jet_amt] == ">" else (-1, 0)
        jet_i += 1

        pushed_pos = move_rock(active_rock, movement)

        if (
            get_min(pushed_pos, 0) >= 0
            and get_max(pushed_pos, 0) <= 6
            and not any(pos in rocks for pos in pushed_pos)
        ):
            active_rock = pushed_pos

        fall_pos = move_rock(active_rock, (0, -1))

        if get_min(fall_pos, 1) <= 0 or any(pos in rocks for pos in fall_pos):
            rocks.update(active_rock)
            highest_y = get_max(rocks, 1)
            active_rock = None
            rock_count += 1
        else:
            active_rock = fall_pos

    return highest_y
