def parse(input: str):
    elves = input.strip().split("\n\n")

    return [[int(x) for x in e.split("\n")] for e in elves]


def part_1(input: list[list[int]]):
    summed = [sum(calories) for calories in input]

    return max(*summed)


def part_2(input: list[list[int]]):
    summed = [sum(calories) for calories in input]

    top_calories = []

    for _ in range(3):
        n = max(*summed)
        summed.remove(n)

        top_calories.append(n)

    return sum(top_calories)
