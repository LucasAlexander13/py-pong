from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color('white')
        self.penup()
        self.goto(0, 240)
        self.score = [0, 0]

    def draw_score(self):
        self.clear()
        self.write(
            arg = f'{self.score[0]}   {self.score[1]}', 
            align ='center', 
            font = ('Bahnschrift', 24, 'normal')
            )