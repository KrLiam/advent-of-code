Pos = tuple[int, int]


def parse(input: str) -> tuple[dict[Pos, tuple[int, int]], list[tuple[Pos, str]]]:
    nums = {}
    symbols = []

    num = ""
    num_incr = 0
    for i, line in enumerate(input.split("\n")):
        # adiciona um caractere falso no fim da linha para a leitura
        # dos numeros nao falhe caso algum numero esteja colado na
        # borda da direita.
        line += "."

        j = 0
        while j < len(line):
            ch = line[j]

            if ch.isdigit():
                num += ch
            elif ch != ".":
                symbols.append(((i, j), ch))

            if num and not ch.isdigit():
                num_obj = (num_incr, int(num))
                num_incr += 1

                for nj in range(j - len(num), j):
                    nums[(i, nj)] = num_obj

                num = ""

            j += 1

    return (nums, symbols)


def get_adjacent_pos(i, j):
    return (
        (i - 1, j - 1),
        (i - 1, j),
        (i - 1, j + 1),
        (i, j - 1),
        (i, j + 1),
        (i + 1, j - 1),
        (i + 1, j),
        (i + 1, j + 1),
    )


def part_1(nums: dict[Pos, tuple[int, int]], symbols: list[tuple[Pos, str]]):
    total_sum = 0

    for (si, sj), _ in symbols:
        numbers = set()

        for adj_i, adj_j in get_adjacent_pos(si, sj):
            if num := nums.get((adj_i, adj_j)):
                numbers.add(num)

        total_sum += sum(num[1] for num in numbers)

    return total_sum


def part_2(nums: dict[Pos, tuple[int, int]], symbols: list[tuple[Pos, str]]):
    total_sum = 0

    for (i, j), ch in symbols:
        if ch != "*":
            continue

        numbers: set[tuple[int, int]] = set()

        for adj_i, adj_j in get_adjacent_pos(i, j):
            if num := nums.get((adj_i, adj_j)):
                numbers.add(num)

        if len(numbers) != 2:
            continue

        (_, a), (_, b) = numbers
        total_sum += a * b

    return total_sum
