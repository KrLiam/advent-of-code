from os import linesep


class Map:
    def __init__(self, lines: list[list[str]]):
        self.lines = lines

    def find_letter(self, letter: str):
        for i, line in enumerate(self.lines):
            if letter in line:
                return (i, line.index(letter))

    def is_inside(self, pos: tuple[int, int]):
        return 0 <= pos[0] < len(self.lines) and 0 <= pos[1] < len(self.lines[0])

    def get(self, pos: tuple[int, int]):
        i, j = pos

        if self.is_inside((i, j)):
            return self.lines[i][j]

    def get_num_height(self, pos: tuple[int, int]):
        letter = self.get(pos)

        if letter == "S":
            return 1
        if letter == "E":
            return 26

        return ord(letter) - 96

    def get_adjacent_pos(
        self,
        pos: tuple[int, int],
        is_climbing=True,
    ):
        i, j = pos
        h = self.get_num_height(pos)

        if is_climbing:
            condition = lambda pos: self.get_num_height(pos) <= h + 1
        else:
            condition = lambda pos: self.get_num_height(pos) >= h - 1

        return [
            adj
            for adj in ((i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1))
            if self.is_inside(adj) and condition(adj)
        ]

    def find_nearest_path(
        self,
        start: tuple[int, int],
        dest: tuple[int, int],
        visited_dist: dict[tuple[int, int], int] = None,
        active: list[tuple[int, int]] = None,
        is_climbing: bool = True,
    ):
        if visited_dist is None:
            visited_dist = {}
        if active is None:
            active = []

        active.append(start)
        visited_dist[start] = 0

        while active:
            pos = active.pop(0)
            this_dist = visited_dist[pos]

            for adj_pos in self.get_adjacent_pos(pos, is_climbing):
                if adj_pos not in visited_dist:
                    visited_dist[adj_pos] = this_dist + 1
                    active.append(adj_pos)

                    if adj_pos == dest:
                        return visited_dist[adj_pos]


def parse(input: str):
    return Map([list(line) for line in input.split(linesep)])


def part_1(map: Map):
    start_pos = map.find_letter("S")
    dest_pos = map.find_letter("E")

    distance = map.find_nearest_path(start_pos, dest_pos)

    return distance


def part_2(map: Map):
    dest_pos = map.find_letter("E")

    visited = {}

    map.find_nearest_path(dest_pos, None, visited, is_climbing=False)

    a_dists = [dist for pos, dist in visited.items() if map.get(pos) in ("S", "a")]

    return a_dists[0]
