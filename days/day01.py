def is_int(char: str) -> bool:
    assert len(char) == 1
    return "0" <= char <= "9"


def part1(data: list[str]):
    """Find first and last integer in each string and print their concatenated sum"""
    values: list[int] = []
    for row in data:
        number_string = ""
        for c in row:
            if is_int(c):
                number_string += c
                break

        for c in row[::-1]:
            if is_int(c):
                number_string += c
                break

        values.append(int(number_string))

    print(sum(values))


def find_number(numbers: dict[str, str], span: str) -> str:
    for num, val in numbers.items():
        if span.startswith(num):
            return val
    else:
        return ""


def part2(data: list[str]):
    """Same as part 1 except 'numbers' could also be spelled in letters"""
    numbers = {
        "zero": "0",
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }
    backwards_numbers = {k[::-1]: v for k, v in numbers.items()}
    longest_num = max(numbers.keys(), key=len)
    number_width = len(longest_num)

    values: list[int] = []
    for row in data:
        row = row.strip()
        number_string = ""
        for i in range(len(row)):
            if is_int(row[i]):
                number_string += row[i]
                break

            span = row[i : i + number_width]
            s = find_number(numbers, span)
            if s:
                number_string += s
                break

        backwards = row[::-1]
        for i in range(len(backwards)):
            if is_int(backwards[i]):
                number_string += backwards[i]
                break

            span = backwards[i : i + number_width]
            s = find_number(backwards_numbers, span)
            if s != "":
                number_string += s
                break

        values.append(int(number_string))

    print(sum(values))
    return values
