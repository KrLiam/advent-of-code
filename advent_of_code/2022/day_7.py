from os import linesep
from typing import Union

from cachetools import cached

Directory = dict[str, Union[int, "Directory"]]


def parse(input: str):
    lines = input.split(linesep)

    path = []
    files: Directory = {}

    for line in lines:
        match line.split(" "):
            case ["$", "cd", arg]:
                if arg == "/":
                    path = []
                elif arg == "..":
                    path.pop()
                else:
                    path.append(arg)
            case [size, name] if size.isdigit():
                size = int(size)

                parent = files
                for dir_name in path:
                    parent = parent.setdefault(dir_name, {})

                parent[name] = size

    return files


@cached({}, key=lambda _, path=(): path)
def compute_size(dir: Directory, path: tuple[str] = ()):
    size = 0

    for dir_name, value in dir.items():
        if isinstance(value, dict):
            size += compute_size(value, (*path, dir_name))
        else:
            size += value

    return size


def part_1(root: Directory):
    compute_size(root)

    sizes = compute_size.cache

    return sum(n for n in sizes.values() if n <= 100_000)


TOTAL_SPACE = 70_000_000
REQUIRED_SPACE = 30_000_000


def part_2(root: Directory):
    compute_size(root)

    sizes = compute_size.cache

    used_space = sizes[()]
    free_space = TOTAL_SPACE - used_space
    missing_space = REQUIRED_SPACE - free_space

    candidates = sorted(size for size in sizes.values() if size >= missing_space)

    return candidates[0]
