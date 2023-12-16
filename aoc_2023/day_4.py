from icecream import ic


def find_hits(game: str) -> list[int]:
    game: list[str] = game.split(":")[1]
    game: list[list[int]] = [list(map(lambda x: int(x), i.split())) for i in game.split("|")]
    u_game, template = game
    hits: list = [i for i in u_game if i in template]
    return hits


def hits_evaluate(game: list[int]) -> int:
    if len(game) < 1:
        return 0
    return 2 ** (len(game) - 1)


def main() -> None:
    with open("aoc_2023/day_4.input", "r") as file:
        result = sum(
            [hits_evaluate(find_hits(i.strip())) for i in file.readlines()]
        )
        print(f"day 4.1: {result}")


if __name__ == "__main__":
    main()
