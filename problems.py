import argparse
import importlib
from pathlib import Path

INPUT_DIR = Path("inputs")
SOLUTIONS_MODULE = "days"


def load_input(file_path: Path) -> list[str]:
    with open(file_path) as f:
        return [line.strip() for line in f.readlines() if not line.isspace()]


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="AdventOfCode2023", description="Advent of code 2023 solution runner"
    )
    parser.add_argument("day", type=int)
    args = parser.parse_args()

    solution_str = f"day{args.day:02}"
    solution = importlib.import_module(f".{solution_str}", SOLUTIONS_MODULE)
    data = load_input(INPUT_DIR / f"{solution_str}.txt")
    print("Solution to part 1")
    solution.part1(data)
    print("Solution to part 2")
    solution.part2(data)
