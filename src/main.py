
class ScoreCard:
    PUNTUATION = {
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
    def __init__(self,throws:str):
        self.throws = throws

    def __repr__(self) -> str:
        return f"{self.throws}"

    def stylizer(self) -> list:
        throws_listed = []
        throws = self.throws.replace('X','XX')
        for position,throw in enumerate(throws):
            if position%2 == 0:
                continue
            if throw == 'X':
                throws_listed.append(throw)
                continue
            throws_listed.append(throws[position-1] + throw)
        return throws_listed

    def Calcutale_frame(self,frame:str) -> int :
        if frame[0] == 'X':
            return 10
        if frame[1] == '-':
            return self.PUNTUATION[frame[0]]
        if frame[1] == '/':
            return self.PUNTUATION[frame[1]]
        return sum(self.PUNTUATION[frame[0]],self.PUNTUATION[frame[1]])

    def Calculate_Score(self) -> int:
        throws = self.stylizer()
        score = 0
        for position,frame in enumerate(throws):
            score += self.Calcutale_frame(frame)
            if frame[1] == '/' or frame[0] == 'X':
                try:
                    score += self.Calcutale_frame(throws[position+1])
                except Exception:
                    continue
            if frame[0] == 'X':
                try:
                    
                    
            


if __name__ == "__main__":
    card1 = ScoreCard("8/549-XX5/53639/9/X")
    print(card1)
    print(card1.stylizer())