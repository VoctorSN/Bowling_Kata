
class ScoreCard:
    INITIAL_SCORE = 0
    def __init__(self,throws:str):
        self.throws = throws

    def Calculate_Score(self):
        score = self.INITIAL_SCORE
        for throw,points in enumerate(self.throws):
            