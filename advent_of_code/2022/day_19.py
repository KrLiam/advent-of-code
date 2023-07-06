import re
from collections import namedtuple
from dataclasses import dataclass
from os import linesep

blueprint_pattern = re.compile(
    r"Blueprint (\d+): "
    + r"Each ore robot costs (\d+) ore. "
    + r"Each clay robot costs (\d+) ore. "
    + r"Each obsidian robot costs (\d+) ore and (\d+) clay. "
    + r"Each geode robot costs (\d+) ore and (\d+) obsidian."
)


@dataclass(frozen=True)
class Blueprint:
    id: int
    ores_orebot: int
    ores_claybot: int
    ores_obsidianbot: int
    clays_obsidianbot: int
    ores_geodebot: int
    obsidians_geodebot: int


def parse(input: str):
    matches = blueprint_pattern.findall(input)

    blueprints = [Blueprint(*map(int, match)) for match in matches]

    return blueprints


def part_1(blueprints: list[Blueprint]):
    for b in blueprints:
        states = []

        states.append((24, 1, 0, 0, 0, 0, 0, 0, 0))

        most_ore_exp_bot = max(
            b.ores_orebot, b.ores_claybot, b.ores_obsidianbot, b.ores_geodebot
        )

        i = 0
        while states:
            state = states.pop(0)
            (
                minutes_left,
                ore_bots,
                clay_bots,
                obsidian_bots,
                geode_bots,
                ores,
                clays,
                obsidians,
                geodes,
            ) = state

            i += 1
            if i % 1_000 == 0:
                print(len(states), state)

            new_minutes_left = minutes_left - 1
            new_ores = ores + ore_bots
            new_clays = clays + clay_bots
            new_obsidians = obsidians + obsidian_bots
            new_geodes = geodes + geode_bots

            def push_state(
                new_minutes_left=new_minutes_left,
                ore_bots=ore_bots,
                clay_bots=clay_bots,
                obsidian_bots=obsidian_bots,
                geode_bots=geode_bots,
                ores=new_ores,
                clays=new_clays,
                obsidians=new_obsidians,
                geodes=new_geodes,
            ):
                states.append(
                    (
                        new_minutes_left,
                        ore_bots,
                        clay_bots,
                        obsidian_bots,
                        geode_bots,
                        ores,
                        clays,
                        obsidians,
                        geodes,
                    )
                )

            bought_ore, bought_clay, bought_obs, bought_geode = (
                False,
                False,
                False,
                False,
            )

            if ore_bots < most_ore_exp_bot and ores >= b.ores_orebot:
                bought_ore = True
                push_state(
                    ore_bots=ore_bots + 1,
                    ores=new_ores - b.ores_orebot,
                )

            if ores >= b.ores_claybot:
                bought_clay = True
                push_state(
                    clay_bots=clay_bots + 1,
                    ores=new_ores - b.ores_claybot,
                )

            if ores >= b.ores_obsidianbot and clays >= b.clays_obsidianbot:
                bought_obs = True
                push_state(
                    obsidian_bots=obsidian_bots + 1,
                    ores=new_ores - b.ores_obsidianbot,
                    clays=new_clays - b.clays_obsidianbot,
                )

            if ores >= b.ores_geodebot and obsidians >= b.obsidians_geodebot:
                bought_geode = True
                push_state(
                    obsidian_bots=obsidian_bots + 1,
                    ores=new_ores - b.ores_geodebot,
                    obsidians=new_obsidians - b.obsidians_geodebot,
                )

            # do nothing
            if not (bought_ore and bought_clay and bought_obs and bought_geode):
                push_state()
