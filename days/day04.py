def count_wins(row: str) -> int:
    _, values = row.split(": ")
    wins, actuals = values.split(" | ")
    win_set = {int(num) for num in wins.split()}
    overlap = list(filter(lambda x: x in win_set, map(int, actuals.split())))
    return len(overlap)


def part1(data: list[str]):
    scores: list[int] = []
    for row in data:
        overlap = count_wins(row)
        score = 2 ** (overlap - 1) if overlap > 0 else 0
        scores.append(score)
    print(sum(scores))


def part2(data: list[str]):
    """Could probably do recursion + memoisation here, but would rather not haha"""
    # First work out all scores, then working backwards get the recursive sum / product
    scores: list[int] = []
    for row in data:
        overlap = count_wins(row)
        scores.append(overlap)

    # card_counts = [int(score > 0) for score in scores]
    card_counts = [1] * len(scores)
    for idx, score in enumerate(scores):
        for card_offset in range(idx + 1, idx + score + 1):
            card_counts[card_offset] += card_counts[idx]

    print(sum(card_counts))
