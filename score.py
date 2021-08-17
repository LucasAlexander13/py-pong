from turtle import Turtle
from time import sleep

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
            arg = f'{self.score[0]}  :  {self.score[1]}', 
            align ='center', 
            font = ('Bahnschrift', 36, 'normal')
            )
    
    def game_over(self, player):
        self.clear()

        self.write(
            arg = f'{self.score[0]}  :  {self.score[1]}', 
            align ='center', 
            font = ('Bahnschrift', 36, 'normal')
            )

        self.goto(0, -40)

        self.write(
            arg = f'  GAME OVER\n{player} WINS', 
            align ='center', 
            font = ('Bahnschrift', 36, 'normal')
            )
        sleep(3)

        self.clear()