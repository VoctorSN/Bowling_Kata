
class ScoreCard:
    INITIAL_GAME_SCORE = 0
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
        for position,throw in enumerate(game):
            if position%2 == 0:
                continue
            if throw == 'X':
                pins.append(throw)
                continue
            pins.append(game[position-1] + throw)
        return pins

    def Calcutale_frame_punctuation(self,frame:str) -> int :
        first_roll = frame[0]
        if len(frame) == 1:
            return self.SCORE_BY_PINS[first_roll]
        second_roll = frame[1]
        if frame[1] == '/':
            return self.SCORE_BY_PINS[second_roll]
        return self.SCORE_BY_PINS[first_roll] + self.SCORE_BY_PINS[second_roll]

    def Calculate_Score(self) -> int:
        game = self.stylizer()
        for position,frame in enumerate(game[:10]):
            if self.is_frame_a_strike_or_spare(frame):
                self.calculate_strike_or_spare(game,frame,position)
            else:
                self.game_score += self.Calcutale_frame_punctuation(frame)
        return self.game_score

    def is_frame_a_strike_or_spare(self,frame:str) -> bool:
        return frame[0] == 'X' or frame[1] == '/'

    def calculate_strike_or_spare(self,game:list,frame:str,position:int) -> None:
        self.game_score += self.Calcutale_frame_punctuation(frame) + self.Calcutale_frame_punctuation(game[position+1][0])
        if frame[0] == 'X':
            if game[position+1] == 'X':
                self.game_score += self.Calcutale_frame_punctuation(game[position+2][0])
                return None
            self.game_score += self.Calcutale_frame_punctuation(game[position+1][1])
            if game[position+1][1] == '/' :
                self.game_score -= self.Calcutale_frame_punctuation(game[position+1][0])
        return None


if __name__ == "__main__":
    card1 = ScoreCard("8/549-XX5/53639/9/X")
    print(card1)
    print(card1.stylizer())
    print(card1.Calculate_Score())