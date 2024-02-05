class ScoreCard:
    __INITIAL_GAME_SCORE = 0

    def Calculate_score(self) -> int:
        """Walks throug the game string stilyzed frame by frame
        andding up the punctuation of the frame and the extra rolls
        to the class variable game_score"""
        game = self.__stylizer()
        for position, frame in enumerate(game[:10]):
            frame = Frame(frame)
            if frame.is_strike():
                self.__calculate_strike(game, frame, position)
            elif frame.is_spare():
                self.__calculate_spare(game, frame, position)
            else:
                self.game_score += frame.calcutale_frame_punctuation()
        return self.game_score

    def __init__(self, game: str):
        self.game_score = self.__INITIAL_GAME_SCORE
        self.game = game

    def __repr__(self) -> str:
        return f"Tu carta es: {' , '.join(self.__stylizer())}"

    def __stylizer(self) -> list:
        """Gives a style to the string given to the class, it splits the string in frames"""
        pins = []
        game = self.game.replace("X", "XX")
        if len(game) == 21:
            game += "-"
        for position in range(1, len(game), 2):
            roll = game[position]
            if Frame(roll).is_strike():
                pins.append(roll)
                continue
            pins.append(game[position - 1] + roll)
        return pins

    def __calculate_strike(self, game: list, frame: str, position: int) -> None:
        """Adds up to the game_score the punctuation of th next 2 rolls"""
        self.__calculate_spare(game, frame, position)
        next_frame = Frame(game[position + 1])
        if next_frame.is_strike():
            second_frame_first_roll = Frame(game[position + 2][0])
            self.game_score += second_frame_first_roll.calcutale_frame_punctuation()
            return None

        second_roll = Frame(game[position + 1][1])
        self.game_score += second_roll.calcutale_frame_punctuation()
        if next_frame.is_spare():
            next_roll = Frame(game[position + 1][0])
            self.game_score -= next_roll.calcutale_frame_punctuation()
        return None

    def __calculate_spare(self, game: list, frame: str, position: int) -> None:
        """Adds up to the game_score the punctuation of the next roll"""
        next_roll = game[position + 1][0]
        self.game_score += (
            Frame(frame).calcutale_frame_punctuation()
            + Frame(next_roll).calcutale_frame_punctuation()
        )


if __name__ == "__main__":
    from frame import Frame

    card1 = ScoreCard("5/5/5/5/5/5/5/5/5/5/5")
    print(card1)
    print(card1.__stylizer())
    print(card1.Calculate_score())
else:
    from src.frame import Frame
