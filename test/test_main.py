from src.main import ScoreCard

def test_repr():
    assert str(ScoreCard("8/549-XX5/53639/1/X")) == 'Tu carta es: 8/ , 54 , 9- , X , X , 5/ , 53 , 63 , 9/ , 1/ , X'

def test_todonumeros():
    assert ScoreCard('12345123451234512345').Calculate_Score() == 60

def test_nueve_fallos():
    assert ScoreCard('9-9-9-9-9-9-9-9-9-9-').Calculate_Score() == 90

def test_numeros_fallos():
    assert ScoreCard("9-3561368153258-7181").Calculate_Score() == 82

def test_numeros_strikes():
    assert ScoreCard('5/5/5/5/5/5/5/5/5/5/5').Calculate_Score() == 150

def test_diferentes():
    assert ScoreCard("12345123451234512345").Calculate_Score() == 60
    assert ScoreCard('9-9-9-9-9-9-9-9-9-9-').Calculate_Score() == 90
    assert ScoreCard('9-3561368153258-7181').Calculate_Score() == 82
    assert ScoreCard("9-3/613/815/-/8-7/8/8").Calculate_Score() == 131
    assert ScoreCard("X9-9-9-9-9-9-9-9-9-").Calculate_Score() == 100
    assert ScoreCard("9-9-9-9-9-9-9-9-9-X9-").Calculate_Score() == 100
    assert ScoreCard("X9-X9-9-9-9-9-9-9-").Calculate_Score() == 110
    assert ScoreCard("XX9-9-9-9-9-9-9-9-").Calculate_Score() == 120
    assert ScoreCard("XXX9-9-9-9-9-9-9-").Calculate_Score() == 141
    assert ScoreCard("9-9-9-9-9-9-9-9-9-XXX").Calculate_Score() == 111
    assert ScoreCard('XXXXXXXXXXXX').Calculate_Score() == 300
    assert ScoreCard("8/549-XX5/53639/9/X").Calculate_Score() == 149
    assert ScoreCard("8/549-XX5/53639/1/X").Calculate_Score() == 141
    assert ScoreCard("X5/X5/XX5/--5/X5/").Calculate_Score() == 175
