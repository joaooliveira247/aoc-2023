def sep_num(string: str) -> tuple[int, str]:
    num = ""
    for char in string:
        if char.isnumeric():
            num += char
    return string.replace(num, ""), int(num)


def sep_games(string: str) -> tuple[int, list[dict[str, int]]]:
    game_id, matches = string.split(":")
    game_id = int(game_id.split(" ")[1])
    matches = matches.replace(" ", "")
    matches = matches.split(";")
    matches = [list(map(lambda x: sep_num(x), i.split(","))) for i in matches]
    matches = [dict(i) for i in matches]
    return game_id, matches


def is_valid_match(match: list[dict[str, int]]) -> list[list[bool]]:
    bag = {"red": 12, "green": 13, "blue": 14}
    new = []
    for i in match:
        a = []
        for k, v in i.items():
            if v <= bag[k]:
                a.append(True)
                continue
            a.append(False)
        new.append(a)
    new_bool = [all(i) for i in new]
    return all(new_bool)


def valid_game(game: str) -> int:
    game_id, games = sep_games(game)
    if is_valid_match(games):
        return game_id
    return 0


def main() -> None:
    with open("aoc_2023/day_2.input", "r") as file:
        print(f"day 2: {sum([valid_game(x.strip()) for x in file.readlines()])}")


if __name__ == "__main__":
    main()
