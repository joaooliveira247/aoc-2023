def get_number_from_string(string: str) -> int:
    chars = [i for i in string if i.isnumeric()]
    return int(chars[0] + chars[-1])


def card_to_num(string: str) -> str:
    numerals = {
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
    new = []
    for i, v in enumerate(string):
        if v.isnumeric():
            new.append((i, v))
    for k, v in numerals.items():
        if (i := string.find(k)) >= 0:
            new.append((i, v))
        if (f := string.rfind(k)) >= 0:
            new.append((f, v))

    new = [z[1] for z in sorted(new)]
    return int(new[0] + new[-1])


def main() -> None:
    with open("aoc_2023/day_1.input", "r") as f:
        lines = f.readlines()
        print(f"day 1.1: {sum([get_number_from_string(i) for i in lines])}")
        print(f"day 1.2: {sum([card_to_num(i) for i in lines])}")


if __name__ == "__main__":
    main()
