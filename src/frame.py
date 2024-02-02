
class Frame:

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
    STRIKE = 'X'
    SPARE = '/'
    def __init__(self,frame:str):
        self.frame = str(frame)

    def __repr__(self) -> str:
        return f'{self.frame}'

    def calcutale_frame_punctuation(self) -> int:
        first_roll = self.frame[0]
        if len(self.frame) == 1:
            return self.SCORE_BY_PINS[first_roll]
        second_roll = self.frame[1]
        if self.is_spare():
            return self.SCORE_BY_PINS[second_roll]
        return self.SCORE_BY_PINS[first_roll] + self.SCORE_BY_PINS[second_roll]

    def is_spare(self) -> bool:
        return self.SPARE in self.frame

    def is_strike(self) -> bool:
        return self.STRIKE in self.frame

if __name__ == '__main__':
    ej=Frame('1-')
    print(ej)
    print(ej.calcutale_frame_punctuation())
