

class ScoreCard:
    INITIAL_GAME_SCORE = 0
    def __init__(self,game:str):
        self.game_score = self.INITIAL_GAME_SCORE
        self.game = game

    def __repr__(self) -> str:
        return f"Tu carta es: {' , '.join(self.stylizer())}"

    def stylizer(self) -> list:
        pins = []
        game = self.game.replace('X','XX')
        if len(game) == 21:
            game += '-'
        for position in range(1,len(game),2):
            roll = game[position]
            if Frame(roll).is_strike():
                pins.append(roll)
                continue
            pins.append(game[position-1] + roll)
        return pins

    def Calculate_Score(self) -> int:
        game = self.stylizer()
        for position,frame in enumerate(game[:10]):
            frame = Frame(frame)
            if frame.is_strike():
                self.calculate_strike(game,frame,position)
            elif frame.is_spare():
                self.calculate_spare(game,frame,position)
            else:
                self.game_score += frame.calcutale_frame_punctuation()
        return self.game_score

    def calculate_strike(self,game:list,frame:str,position:int) -> None:
        self.calculate_spare(game,frame,position)
        if Frame(game[position+1]).is_strike():
            self.game_score += Frame(game[position+2][0]).calcutale_frame_punctuation()
            return None
        self.game_score += Frame(game[position+1][1]).calcutale_frame_punctuation()
        if Frame(game[position+1]).is_spare() :
            self.game_score -= Frame(game[position+1][0]).calcutale_frame_punctuation()
        return None

    def calculate_spare(self,game:list,frame:str,position:int) -> None:
        next_roll = game[position+1][0]
        self.game_score += Frame(frame).calcutale_frame_punctuation() + Frame(next_roll).calcutale_frame_punctuation()




if __name__ == "__main__":
    from frame import Frame
    card1 = ScoreCard('5/5/5/5/5/5/5/5/5/5/5')
    print(card1)
    print(card1.stylizer())
    print(card1.Calculate_Score())
else:
    from src.frame import Frame