from turtle import Turtle

class Paddle():
    def __init__(self, position):
        self.paddle = []
        self.draw_paddle(position)

    def draw_paddle(self, position):
        for i in range(5):
            segment = Turtle()
            segment.shape('square')
            segment.speed('fastest')
            segment.color('white')
            segment.penup()

            if position == 'right':
                segment.goto(360, i * -20)
                self.paddle.append(segment)
            
            elif position == 'left':
                segment.goto(-360, i * 20)
                self.paddle.append(segment)

    def go_up(self):
        for i in range(len(self.paddle)):
            self.paddle[i].setheading(90)
            self.paddle[i].forward(20)

    def go_down(self):
        for i in range(len(self.paddle)):
            self.paddle[i].setheading(270)
            self.paddle[i].forward(20)
