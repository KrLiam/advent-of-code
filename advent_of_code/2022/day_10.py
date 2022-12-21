from os import linesep


def parse(input: str):
    lines = input.split(linesep)

    result = []
    for line in lines:
        cmd, *args = line.split(" ")
        result.append((cmd, *map(int, args)))

    return result


INSTRUCTION_DELAY = {
    "addx": 2,
    "noop": 1,
}


def program(instructions: list[tuple[str, int]]):
    instructions = list(instructions)

    X = 1
    signal_strengths = 0
    counter = 0

    instruction_delay = 0
    instruction = None
    args = None

    while instructions:
        counter += 1

        if (counter - 20) % 40 == 0:
            signal_strengths += counter * X

        yield (counter, X, signal_strengths)

        if not instruction:
            instruction, *args = instructions.pop(0)
            instruction_delay = INSTRUCTION_DELAY[instruction]

        instruction_delay -= 1

        if instruction_delay <= 0:
            match instruction:
                case "addx":
                    X += args[0]
                case "noop":
                    ...

            instruction = None


def part_1(instructions: list[tuple[str, int]]):
    prog = program(instructions)

    while res := next(prog, None):
        _, _, signal_strengths = res

    return signal_strengths


WIDTH = 40
HEIGHT = 6


def part_2(instructions: list[tuple[str, int]]):
    prog = program(instructions)

    crt = []
    row = []

    while res := next(prog, None):
        counter, X, _ = res
        pos = (counter - 1) % WIDTH

        row.append("💀" if abs(X - pos) <= 1 else "  ")

        if len(row) >= WIDTH:
            crt.append(row)
            row = []

    return linesep * 2 + linesep.join("".join(r) for r in crt) + linesep
