from collections import defaultdict
import math

EXCLUDED = "."
GEAR = "*"


def get_shape(data: list[str]) -> tuple[int, int]:
    n_rows = len(data)
    n_cols = len(data[0])
    for row in data:
        assert len(row) == n_cols
    return n_rows, n_cols


def part1(data: list[str]):
    """Find numbers in a grid that are horizontally, vertically or diagonally adjacent
    to a special character"""
    n_rows, n_cols = get_shape(data)
    part_numbers: list[int] = []
    for i, row in enumerate(data):
        span_start, span_end = -1, -1
        j = 0
        while j < n_cols:
            # 1. find numeric spans
            if row[j].isnumeric():
                span_start = j
                span_end = k = span_start + 1
                while row[j:k].isnumeric() and k <= n_cols:
                    span_end = k
                    k += 1
                j = span_end
                number = int(row[span_start:span_end])
                # print(number)
                # 2. Numeric span found, generate possible search candidates
                # searching columnwise left to right
                for adjacent_i in (i - 1, i, i + 1):
                    if adjacent_i < 0 or adjacent_i >= n_rows:
                        continue
                    for adjacent_j in range(span_start - 1, span_end + 1):
                        if adjacent_j < 0 or adjacent_j >= n_cols:
                            continue

                        char = data[adjacent_i][adjacent_j]
                        if char != EXCLUDED and not char.isalnum():
                            part_numbers.append(number)
            else:
                j += 1
    print(sum(part_numbers))


def part2(data: list[str]):
    """Annoyingly I got unlucky and took the non-scalable appraoch for p1.
    We now need to find all '*' characters that are adjacent to exactly two numbers,
    and return the sums of their product.
    """
    n_rows, n_cols = get_shape(data)
    # Find all gears each number is connected to
    gears: dict[tuple[int, int], list[int]] = defaultdict(list)
    for i, row in enumerate(data):
        span_start, span_end = -1, -1
        j = 0
        while j < n_cols:
            # 1. find numeric spans
            if row[j].isnumeric():
                span_start = j
                span_end = k = span_start + 1
                while row[j:k].isnumeric() and k <= n_cols:
                    span_end = k
                    k += 1
                j = span_end
                number = int(row[span_start:span_end])
                # 2. Numeric span found, generate possible search candidates
                # searching columnwise left to right
                for adjacent_i in (i - 1, i, i + 1):
                    if adjacent_i < 0 or adjacent_i >= n_rows:
                        continue
                    for adjacent_j in range(span_start - 1, span_end + 1):
                        if adjacent_j < 0 or adjacent_j >= n_cols:
                            continue
                        char = data[adjacent_i][adjacent_j]
                        if char == GEAR:
                            gears[(adjacent_i, adjacent_j)].append(number)
            else:
                j += 1

    ratio_total = sum(
        [math.prod(ratios) for ratios in gears.values() if len(ratios) == 2]
    )
    print(ratio_total)
