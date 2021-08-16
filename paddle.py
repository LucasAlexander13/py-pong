from turtle import Turtle, color

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        # Defines paddle attributes
        self.shape('square')
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.color('white')
        self.setheading(90)
        self.penup()

        # Set initial position
        if position == 'right':
            self.goto(360, -20)
        
        elif position == 'left':
            self.goto(-360, 20)

    def go_up(self):
        if self.ycor() <= 140:
            self.forward(20)

    def go_down(self):
        if self.ycor() >= -140:
            self.forward(-20)
