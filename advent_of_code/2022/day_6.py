def find_end_of_marker(stream: str, length: int):
    for i in range(length - 1, len(stream)):
        if len(set(stream[i - length + 1 : i + 1])) == length:
            return i + 1  # ordinal position


def part_1(stream: str):
    return find_end_of_marker(stream, 4)


def part_2(stream: str):
    return find_end_of_marker(stream, 14)
