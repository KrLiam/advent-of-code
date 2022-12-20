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


def get_min(rock: list[tuple[int, int]], axis: int):
    return min(pos[axis] for pos in rock)


def get_max(rock: list[tuple[int, int]], axis: int):
    return max(pos[axis] for pos in rock)


def print_rocks(rocks: set[tuple[int, int]]):
    highest_y = get_max(rocks, 1)

    for y in range(highest_y, 0, -1):
        print("\n".join("#" if (x, y) in rocks else "." for x in range(0, 7)))


def simulation(jets: list[str], rock_amount: int, rocks: set[tuple[int, int]] = None):
    rocks = set() if rocks is None else rocks
    rock_i = 0
    jet_i = 0
    jet_amt = len(jets)

    active_rock = None
    highest_y = 0
    rock_count = 0

    while rock_count < rock_amount:
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

        yield jet_i, jet_amt, rock_count, highest_y


def part_1(jets: list[str]):
    for _, _, _, highest_y in simulation(jets, 2022):
        ...

    return highest_y


def part_2(jets: list[str]):
    jet_amt = len(jets)

    samples = []
    total_rocks = 1_000_000_000_000
    total_y = 0

    waiting_rest = False

    for jet_i, jet_amt, rocks, highest_y in simulation(jets, 69696969):
        if jet_i % jet_amt == 0:
            samples.append((rocks, highest_y))

            if len(samples) < 2:
                continue

            (rocks_a, y_a), (rocks_b, y_b) = samples

            rocks_by_interval = rocks_b - rocks_a
            y_increase_by_interval = y_b - y_a

            total_rocks -= rocks_a
            total_y += y_a

            interval_repeat = total_rocks // rocks_by_interval
            interval_rest = total_rocks % rocks_by_interval

            waiting_rest = True

        if waiting_rest and rocks >= (rocks_b + interval_rest):
            rest_y = highest_y - y_b
            break

    total_rocks -= interval_repeat * rocks_by_interval + interval_rest
    total_y += interval_repeat * y_increase_by_interval + rest_y

    return total_y
