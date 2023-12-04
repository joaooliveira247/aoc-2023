from aoc_2023.day_1 import get_number_from_string, card_to_num


def test_day_1() -> None:
    nums = [
        get_number_from_string(i)
        for i in ["1abc2", "pqr3stu8vwx", "a1b2c3d4e5f", "treb7uchet"]
    ]
    assert sum(nums) == 142


def test_day_1_2() -> None:
    nums = [
        card_to_num(i)
        for i in [
            "two1nine",
            "eightwothree",
            "abcone2threexyz",
            "xtwone3four",
            "4nineeightseven2",
            "zoneight234",
            "7pqrstsixteen",
        ]
    ]
    print(nums)
    assert sum(nums) == 281


def test_day_1_2_others_inputs() -> None:
    nums = [
        card_to_num(i)
        for i in [
            "92threesix89",
            "ninesixnine",
            "khvptwo7kkbznndpqsevensevenvlr",
            "2v",
            "9mqxcrjxnp7hdjgqktxm",
            "eight298",
            "zjrnmhclxhrkjpffhxkthnvj83jnshbqvx",
        ]
    ]
    assert nums == [99, 99, 27, 22, 97, 88, 83]


def test_day_1_2_another_inputs() -> None:
    original_numbers = [
        27,
        61,
        22,
        13,
        53,
        39,
        88,
        59,
        44,
        23,
        91,
        33,
        78,
        69,
        55,
        88,
        21,
        11,
        55,
        98,
        49,
        42,
        52,
        12,
        47,
        77,
        17,
        76,
        99,
        99,
        39,
        11,
        33,
        89,
        36,
        33,
        32,
        88,
        39,
        55,
        84,
        66,
        77,
        46,
        11,
        47,
        22,
        54,
        74,
        81,
        82,
        88,
        88,
        48,
        53,
        47,
        22,
        61,
    ]

    decoded_strings = [
        "bhfhszrhzgrhsfd2threeseventwosevenoneseven",
        "hhc6onegvkgkqs5mvsone",
        "jtgpzjjtwo86seventwo",
        "15eightonethreesixthree",
        "56seven98three4three",
        "3ninejbszdvdgznfourxpcxspqxnthlngkncvnineccq",
        "eightsevensevenlmbjzprggthree1eight",
        "fivetwo6nine1tdczktmfninelrbnnine",
        "fournineseven6fourfour",
        "25dpfsrbcllhtwothree2pthreezfhjx",
        "dcfggnine1onetwoone",
        "threeseven7tshthree",
        "7one1sixeighttxcnhltwooneeight",
        "szsvdzsix3nine32nine",
        "five5tkgb8rrztmcfivebknjd",
        "eight9sixgfvhvlcnineeight",
        "tgrglqfxxc2onetwo76oneonex",
        "one48one",
        "five523fivecbs",
        "hrsrszgrcl9seven8eightksdnhqsq7eight",
        "fourmm61nine558nine",
        "bxfour3two2sb4twondmfdpsz",
        "5fiveonefour8lhqmltwoeighttwo",
        "vxrrlfnlqf1twoeightninesixonetwo",
        "k4bftq68seven4nineseven",
        "drgttpqpsevenvrkxdlmvtctsc72seven",
        "onefivesevenfsmmhkbcplj6seven",
        "7foursixbrcc6twosixgnf",
        "ninexzznsix5nine",
        "ninentdd6qvkclninefivenine",
        "threeninefourpmtmlgllftnvxzn5twonine",
        "zkoneight99jrrmgsfpsixfiveone",
        "threevklcphgkjsnine4eight4fmtffknglthree",
        "xkqqlmfmrveightsix4nine93nine",
        "3foursevensix6cksix5six",
        "three8five7xxthreebqrbx",
        "flcpl3btfmbbpnkjvnlmcthreetwo1eightwops",
        "eightprbxpj5oneightcxj",
        "threeeight16nine2mzhxnine",
        "fivesix8five",
        "81fouronenine489four",
        "sixnklrjbeightn2six",
        "kpxkbbxseveneight89sevenrbhqqpk",
        "zzkbtkghmmqfourrtsixxxfjnvvccmpsd5six",
        "onenzlhvtdgkjmjgldmddhngdv9onebkt",
        "4hgdxjgbn1sixseven7twosixseven",
        "two1dntwo",
        "5foureightfourfcs",
        "seventwozjqszlhzxlpgphnkz2foursixfour",
        "8flntwomkktkpvsone78sixone",
        "8fiveeightonetwovgvhzgzfjh16eightwohlk",
        "eight7qvgkbk238fiveeight",
        "lnseightnine9eight",
        "mkbgbkvzdpzxfmrhdcjklxfoureightzzpn3eight",
        "xdglmrpxbz5xpjxzpmvrgsixthreeseven7threebtqfkqp",
        "four35seven7onenvdsevenftnpbcj",
        "twofive4eightwozz",
        "rmjvhrjjmkqsn6gqthreeonefivemxqhrzvffone",
    ]

    nums = [card_to_num(i) for i in decoded_strings]
    assert nums == original_numbers

def test_day_1_2_one_eight() -> None:
    assert card_to_num("oneight") == 18
