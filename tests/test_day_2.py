from aoc_2023.day_2 import valid_game, sep_num, sep_games, is_valid_match


def test_valid_game() -> None:
    input: list[str] = [
        "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
        "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
        "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
        "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
        "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green",
    ]

    assert sum([valid_game(i) for i in input]) == 8


def test_sep_num() -> None:
    assert sep_num("12green") == ("green", 12)


def test_sep_games() -> None:
    test_game: str = "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"
    assert sep_games(test_game) == (
        1,
        [
            {"blue": 3, "red": 4},
            {"red": 1, "green": 2, "blue": 6},
            {"green": 2},
        ],
    )


def test_is_valid_match() -> None:
    test_game: list[dict[str, int]] = [
        {"blue": 3, "red": 4},
        {"red": 1, "green": 2, "blue": 6},
        {"green": 2},
    ]
    assert is_valid_match(test_game) == True

def test_is_invalid_match() -> None:
    test_game: list[dict[str, int]] = [
            {"blue": 3, "red": 4},
            {"red": 19, "green": 2, "blue": 6},
            {"green": 27},
        ]
    
    assert is_valid_match(test_game) == False
