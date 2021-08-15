from turtle import Turtle

class Ball(Turtle):
    def __init__(self,):
        super().__init__()
        # Defines paddle attributes
        self.shape('square')
        self.shapesize(stretch_wid=0.8)
        self.color('white')
        self.penup()
