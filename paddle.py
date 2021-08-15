from turtle import Turtle, color

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        # Defines paddle attributes
        self.shape('square')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color('white')
        self.penup()

        # Set initial position
        if position == 'right':
            self.goto(360, -20)
        
        elif position == 'left':
            self.goto(-360, 20)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
