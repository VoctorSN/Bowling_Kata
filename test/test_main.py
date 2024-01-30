from src.main import ScoreCard

def test_todonumeros():
    card = ScoreCard('12345123451234512345')
    assert card.Calculate_Score() == 60

def test_nueve_fallos():
    assert ScoreCard('9-9-9-9-9-9-9-9-9-9-').Calculate_Score() == 90

def test_numeros_fallos():
    assert ScoreCard("9-3561368153258-7181").Calculate_Score() == 82

def test_numeros_strikes():
    card = ScoreCard('5/5/5/5/5/5/5/5/5/5/5')
    assert card.Calculate_Score() == 150

"""
TotalScoreHittingPinsTest() {

		# Hitting pins total = 60
		pins = "12345123451234512345";
		int total = 60;
		scoreCard = ScoreCard(pins);
		scoreCard.calculateScore();
		assertEquals(total, scoreCard.getTotalScore());
	}

TotalScoreHittingPinsFailTest() {

		// test symbol -

		pins = "9-9-9-9-9-9-9-9-9-9-";
		total = 90;
		scoreCard = ScoreCard(pins);
		scoreCard.calculateScore();
		assertEquals(total, scoreCard.getTotalScore());

		pins = "9-3561368153258-7181";
		total = 82;
		scoreCard = ScoreCard(pins);
		scoreCard.calculateScore();
		assertEquals(total, scoreCard.getTotalScore());
	}

TotalScoreSpareTest() {
		/* 	
		 * If in two tries he knocks them all down, this is called
		 * a “spare” and his score for the frame is ten plus the
		 * number of pins knocked down on his next throw (in
		 * his next turn).
		 * If he gets a spare or strike in the last (tenth) frame,
		 * the bowler gets to throw one or two more bonus balls,
		 * respectively. - These bonus throws are taken as part of
		 * the same turn. If the bonus throws knock down all the
		 * pins, the process does not repeat: the bonus throws are
		 * only used to calculate the score of the final frame.
		 */

		pins = "5/5/5/5/5/5/5/5/5/5/5";
		total = 150;
		scoreCard = ScoreCard(pins);
		scoreCard.calculateScore();
		assertEquals(total, scoreCard.getTotalScore());

		pins = "9-3/613/815/-/8-7/8/8";
		total = 131;
		scoreCard = ScoreCard(pins);
		scoreCard.calculateScore();
		assertEquals(total, scoreCard.getTotalScore());
	}

TotalScoreStrikeTest() {
		/* If on his first try in the frame he knocks down all the
		 * pins, this is called a “strike”. His turn is over, and his
		 * score for the frame is ten plus the simple total of the
		 * pins knocked down in his next two rolls.
		 * If he gets a spare or strike in the last (tenth) frame,
		 * the bowler gets to throw one or two more bonus balls,
		 * respectively. - These bonus throws are taken as part of
		 * the same turn. If the bonus throws knock down all the
		 * pins, the process does not repeat: the bonus throws are
		 * only used to calculate the score of the final frame.
		 */

		pins = "X9-9-9-9-9-9-9-9-9-";
		total = 100;
		scoreCard = ScoreCard(pins);
		scoreCard.calculateScore();
		assertEquals(total, scoreCard.getTotalScore());

		// two extra final rolls
		pins = "9-9-9-9-9-9-9-9-9-X9-";
		total = 100;
		scoreCard = ScoreCard(pins);
		scoreCard.calculateScore();
		assertEquals(total, scoreCard.getTotalScore());

		pins = "X9-X9-9-9-9-9-9-9-";
		total = 110;
		scoreCard = ScoreCard(pins);
		scoreCard.calculateScore();
		assertEquals(total, scoreCard.getTotalScore());

		// two strikes in a row is a double
		pins = "XX9-9-9-9-9-9-9-9-";
		total = 120;
		scoreCard = ScoreCard(pins);
		scoreCard.calculateScore();
		assertEquals(total, scoreCard.getTotalScore());

		// three strikes in a row is a triple
		pins = "XXX9-9-9-9-9-9-9-";
		total = 141;
		scoreCard = ScoreCard(pins);
		scoreCard.calculateScore();
		assertEquals(total, scoreCard.getTotalScore());

		// two strikes in extra rolls
		pins = "9-9-9-9-9-9-9-9-9-XXX";
		total = 111;
		scoreCard = ScoreCard(pins);
		scoreCard.calculateScore();
		assertEquals(total, scoreCard.getTotalScore());

		// 12 strikes is a “Thanksgiving Turkey”.
		pins = "XXXXXXXXXXXX";
		total = 300;
		scoreCard = ScoreCard(pins);
		scoreCard.calculateScore();
		assertEquals(total, scoreCard.getTotalScore());

		// spare in extra roll
		pins = "8/549-XX5/53639/9/X";
		total = 149;
		scoreCard = ScoreCard(pins);
		scoreCard.calculateScore();
		assertEquals(total, scoreCard.getTotalScore());

		// spare in extra roll
		pins = "X5/X5/XX5/--5/X5/";
		total = 175;
		scoreCard = ScoreCard(pins);
		scoreCard.calculateScore();
		assertEquals(total, scoreCard.getTotalScore());

}
"""

