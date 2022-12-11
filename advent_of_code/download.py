from functools import cache
from pathlib import Path

import requests


@cache
def request_input(year: int, day: int):
    url = f"https://adventofcode.com/{year}/day/{day}/input"

    res = requests.get(url)

    if not res.ok:
        raise ValueError("Invalid input arguments.")

    return res.text


@cache
def load_input(year: int, day: int):
    name = f"day_{day}.txt"

    root_dir = Path(__file__).parent
    file = root_dir / f"{year}/inputs/{name}"

    if file.exists():
        return file.read_text()

    txt = request_input(year, day)

    file.parent.mkdir(parents=True, exist_ok=True)
    file.write_text(txt)

    return txt
