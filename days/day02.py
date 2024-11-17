import math

RED = 12
GREEN = 13
BLUE = 14

LIMITS = {
    "red": RED,
    "green": GREEN,
    "blue": BLUE,
}


def part1(data: list[str]):
    """Find the sum of all game id's where we never exceed the pre-defined colour limits
    in any single round / observation"""
    valid_games: list[int] = []
    for row in data:
        game, observations = row.split(": ")
        game_id = int(game.split()[-1])
        observation_sets = observations.split("; ")
        valid = True
        for set in observation_sets:
            counts = set.split(", ")
            for c in counts:
                count, colour = c.split()
                if int(count) > LIMITS[colour]:
                    valid = False
        if valid:
            valid_games.append(game_id)

    print(sum(valid_games))


def part2(data: list[str]):
    """Instead now find the minimum amount of cubes for each colour to make the game
    possible, return the sum of the products of min cubes for all games"""
    powers = []
    for row in data:
        max_counts = {
            "red": 1,
            "green": 1,
            "blue": 1,
        }
        _, observations = row.split(": ")
        observation_sets = observations.split("; ")
        for set in observation_sets:
            counts = set.split(", ")
            for c in counts:
                count, colour = c.split()
                max_counts[colour] = max(int(count), max_counts[colour])
        powers.append(math.prod(max_counts.values()))

    print(sum(powers))
