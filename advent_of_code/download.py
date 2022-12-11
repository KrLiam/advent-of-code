import webbrowser
from functools import cache
from os import linesep
from pathlib import Path


@cache
def request_input(year: int, day: int):
    url = f"https://adventofcode.com/{year}/day/{day}/input"

    input(
        "Seems like the input file for this puzzle is missing.\n\n"
        + f"Opening '{url}' on the browser. Press any key to proceed."
    )

    print("Copy and paste the input text here, then press Ctrl + D to continue:")

    webbrowser.open(url)

    lines = []
    while True:
        try:
            line = input()
        except EOFError:
            break
        lines.append(line)

    print("\nSuccessfuly loaded input text.\n")

    return linesep.join(lines)


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
