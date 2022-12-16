from os import linesep


def parse(input: str):
    lines = input.split(linesep)

    return [[*map(int, line)] for line in lines]


def is_visible(trees: list[list[int]], i: int, j: int):
    max_i = len(trees) - 1
    max_j = len(trees[0]) - 1

    if i == 0 or i == max_i or j == 0 or j == max_j:
        return True

    this_height = trees[i][j]
    row = trees[i]
    column = [trees[n][j] for n in range(max_i + 1)]

    for side in (row[:j], row[j + 1 :], column[:i], column[i + 1 :]):
        if all(h < this_height for h in side):
            return True

    return False


def part_1(trees: list[list[int]]):
    return sum(
        is_visible(trees, i, j) for i in range(len(trees)) for j in range(len(trees[0]))
    )


def get_view_distance(trees: list[list[int]], i: int, j: int):
    this_height = trees[i][j]
    row = trees[i]
    column = [trees[n][j] for n in range(len(trees))]

    score = 1

    for side in (row[j - 1 :: -1], row[j + 1 :], column[i - 1 :: -1], column[i + 1 :]):
        n = 0

        for h in side:
            n += 1

            if h >= this_height:
                break

        score *= n

    return score


def part_2(trees: list[list[int]]):
    return max(
        get_view_distance(trees, i, j)
        for i in range(len(trees))
        for j in range(len(trees[0]))
    )
