class Frame:
    __SCORE_BY_PINS = {
        "1": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "X": 10,
        "/": 10,
        "-": 0,
    }
    STRIKE = "X"
    SPARE = "/"

    def calcutale_frame_punctuation(self) -> int:
        """Returns a integer depending of the frame not caring if it has extra rolls or not"""
        first_roll = self.frame[0]
        if len(self.frame) == 1:
            return self.__SCORE_BY_PINS[first_roll]
        second_roll = self.frame[1]
        if self.is_spare():
            return self.__SCORE_BY_PINS[second_roll]
        return self.__SCORE_BY_PINS[first_roll] + self.__SCORE_BY_PINS[second_roll]

    def is_spare(self) -> bool:
        """Return if the frame is a spare or not"""
        return self.SPARE in self.frame

    def is_strike(self) -> bool:
        """Return if the frame is a strike or not"""
        return self.STRIKE in self.frame

    def __init__(self, frame: str):
        self.frame = repr(frame).replace("'", "")

    def __str__(self) -> str:
        return f"Este frame es: |{self.frame[0]},{self.frame[1]}|"

    def __repr__(self):
        return f"{self.frame}"


if __name__ == "__main__":
    frame_ejemplo = Frame("1-")
    print(frame_ejemplo)
    print(frame_ejemplo.calcutale_frame_punctuation())
