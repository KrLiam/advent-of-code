from typing import Literal


Color = Literal["red", "blue", "green"]
Game = tuple[int, list[dict[Color, int]]]


def parse(input: str) -> list[Game]:
    games = []

    for line in input.split("\n"):
        game, rounds_str = line.split(":")
        _, game_num_str = game.split(" ")

        game_num = int(game_num_str)

        rounds = []
        for round in rounds_str.split(";"):
            subsets = [subset.strip().split(" ") for subset in round.split(", ")]
            rounds.append({color: int(num) for num, color in subsets})

        games.append((game_num, rounds))

    return games


def part_1(games: list[Game]):
    sum = 0

    for num, rounds in games:
        if any(
            subset.get("red", 0) > 12
            or subset.get("green", 0) > 13
            or subset.get("blue", 0) > 14
            for subset in rounds
        ):
            continue

        sum += num

    return sum


def part_2(games):
    sum = 0

    for _, rounds in games:
        red = max(subset.get("red", 0) for subset in rounds)
        green = max(subset.get("green", 0) for subset in rounds)
        blue = max(subset.get("blue", 0) for subset in rounds)

        power = red * green * blue
        sum += power
        print(f"power is {power}")
    
    return sum
