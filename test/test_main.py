from src.score_card import ScoreCard


def test_repr():
    assert (
        repr(ScoreCard("8/549-XX5/53639/1/X"))
        == "Tu carta es: 8/ , 54 , 9- , X , X , 5/ , 53 , 63 , 9/ , 1/ , X"
    )


def test_todonumeros():
    assert ScoreCard("12345123451234512345").Calculate_score() == 60


def test_nueve_fallos():
    assert ScoreCard("9-9-9-9-9-9-9-9-9-9-").Calculate_score() == 90


def test_numeros_fallos():
    assert ScoreCard("9-3561368153258-7181").Calculate_score() == 82


def test_numeros_strikes():
    assert ScoreCard("5/5/5/5/5/5/5/5/5/5/5").Calculate_score() == 150


def test_diferentes():
    assert ScoreCard("12345123451234512345").Calculate_score() == 60
    assert ScoreCard("9-9-9-9-9-9-9-9-9-9-").Calculate_score() == 90
    assert ScoreCard("9-3561368153258-7181").Calculate_score() == 82
    assert ScoreCard("9-3/613/815/-/8-7/8/8").Calculate_score() == 131
    assert ScoreCard("X9-9-9-9-9-9-9-9-9-").Calculate_score() == 100
    assert ScoreCard("9-9-9-9-9-9-9-9-9-X9-").Calculate_score() == 100
    assert ScoreCard("X9-X9-9-9-9-9-9-9-").Calculate_score() == 110
    assert ScoreCard("XX9-9-9-9-9-9-9-9-").Calculate_score() == 120
    assert ScoreCard("XXX9-9-9-9-9-9-9-").Calculate_score() == 141
    assert ScoreCard("9-9-9-9-9-9-9-9-9-XXX").Calculate_score() == 111
    assert ScoreCard("XXXXXXXXXXXX").Calculate_score() == 300
    assert ScoreCard("8/549-XX5/53639/9/X").Calculate_score() == 149
    assert ScoreCard("8/549-XX5/53639/1/X").Calculate_score() == 141
    assert ScoreCard("X5/X5/XX5/--5/X5/").Calculate_score() == 175
