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
