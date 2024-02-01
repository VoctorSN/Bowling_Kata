
class ScoreCard:
    INITIAL_GAME_SCORE = 0
    STRIKE = 'X'
    SPARE = '/'
    SCORE_BY_PINS = {
        '1':1,
        '2':2,
        '3':3,
        '4':4,
        '5':5,
        '6':6,
        '7':7,
        '8':8,
        '9':9,
        'X':10,
        '/':10,
        '-':0
    }
    def __init__(self,game:str):
        self.game_score = self.INITIAL_GAME_SCORE
        self.game = game

    def __repr__(self) -> str:
        return f"{' , '.join(self.stylizer())}"

    def stylizer(self) -> list:
        pins = []
        game = self.game.replace('X','XX')
        if len(game) == 21:
            game += '-'
        for position in range(1,len(game),2):
            roll = game[position]
            if self.is_strike(roll):
                pins.append(roll)
                continue
            pins.append(game[position-1] + roll)
        return pins

    def Calcutale_frame_punctuation(self,frame:str) -> int :
        first_roll = frame[0]
        if len(frame) == 1:
            return self.SCORE_BY_PINS[first_roll]
        second_roll = frame[1]
        if self.is_spare(frame):
            return self.SCORE_BY_PINS[second_roll]
        return self.SCORE_BY_PINS[first_roll] + self.SCORE_BY_PINS[second_roll]

    def Calculate_Score(self) -> int:
        game = self.stylizer()
        for position,frame in enumerate(game[:10]):
            if self.is_strike(frame):
                self.calculate_strike(game,frame,position)
            elif self.is_spare(frame):
                self.calculate_spare(game,frame,position)
            else:
                self.game_score += self.Calcutale_frame_punctuation(frame)
        return self.game_score

    def calculate_strike(self,game:list,frame:str,position:int) -> None:
        self.calculate_spare(game,frame,position)
        if self.is_strike(game[position+1]):
            self.game_score += self.Calcutale_frame_punctuation(game[position+2][0])
            return None
        self.game_score += self.Calcutale_frame_punctuation(game[position+1][1])
        if self.is_spare(game[position+1]) :
            self.game_score -= self.Calcutale_frame_punctuation(game[position+1][0])
        return None

    def calculate_spare(self,game:list,frame:str,position:int) -> None:
        next_roll = game[position+1][0]
        self.game_score += self.Calcutale_frame_punctuation(frame) + self.Calcutale_frame_punctuation(next_roll)

    def is_strike(self,frame:str) -> bool:
        return self.STRIKE in frame

    def is_spare(self,frame:str) -> bool:
        return self.SPARE in frame


if __name__ == "__main__":
    card1 = ScoreCard("8/549-XX5/53639/9/X")
    print(card1)
    print(card1.stylizer())
    print(card1.Calculate_Score())