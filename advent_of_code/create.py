from pathlib import Path

from .download import load_input


TEMPLATE = """
def parse(txt: str) -> Fixme:
    ...

def part_1(fixme: Fixme) -> int:
    ...

def part_2(fixme: Fixme) -> int:
    ...
"""


def create_solution(year: int, day: int):
    load_input(year, day)

    root_dir = Path(__file__).parent
    script = root_dir / f"{year}/day_{day}.py"

    if script.exists():
        return

    script.parent.mkdir(parents=True, exist_ok=True)
    script.write_text(TEMPLATE, encoding="utf-8")
