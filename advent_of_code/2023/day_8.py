
from typing import Callable, Iterable, TypeVar


def parse(txt: str) -> tuple[str, dict[str, tuple[str, str]]]:
    directions, network = txt.split("\n\n")

    nodes: dict[str, tuple[str, str]] = {}
    for line in network.split("\n"):
        origin, dest = line.split(" = ")
        nodes[origin] = tuple(dest[1:-1].split(", "))
    
    return directions, nodes


def part_1(directions: str, nodes: dict[str, tuple[str, str]]) -> int:
    current = "AAA"
    steps = 0

    while current != "ZZZ":
        d = directions[steps % len(directions)]
        steps += 1
        dest = nodes[current]
        current = dest[0 if d == "L" else 1]
    
    return steps


def find_cycle(
    start: str, directions: str, nodes: dict[str, tuple[str, str]]
):
    visited = []

    current = start
    i = 0
    while (current, i) not in visited:
        visited.append((current, i))

        dest = nodes[current]
        d = directions[i]
        current = dest[0 if d == "L" else 1]
        i = (i + 1) % len(directions)
    
    visited.append((current, i))
    # print(visited)
    
    return visited



T = TypeVar("T")
def find(array: Iterable[T], predicate: Callable[[T], bool]) -> int:
    for i, el in enumerate(array):
        if predicate(el):
            return i
    
    return -1


def part_2(directions: str, nodes: dict[str, tuple[str, str]]) -> int:
    initial_nodes = [node for node in nodes.keys() if node.endswith("A")]

    cycles = []
    for node in initial_nodes:
        visited = find_cycle(node, directions, nodes)
        start = visited.index(visited[-1])
        size = len(visited) - start - 1
        cycles.append((start, size))
        print(f"loop startning: {start}, loop size: {size}")
    
    current = [start for start, _ in cycles]

    max_size = max(size for _, size in cycles)
    longest_cycle_i = find(cycles, lambda cycle: cycle[1] == max_size)

    while True:
        current[longest_cycle_i] += cycles[longest_cycle_i][1]

        highest = max(current)

        for i in range(0, len(current)):
            _, size = cycles[i]
            repetitions = (highest - current[i]) // size
            current[i] += size * repetitions
        
        if all(current[0] == node for node in current):
            break
    
    print(current)