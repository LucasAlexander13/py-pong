from turtle import Turtle

class Ball(Turtle):
    def __init__(self,):
        super().__init__()
        # Defines paddle attributes
        self.shape('square')
        self.shapesize(stretch_wid=0.8)
        self.color('white')
        self.penup()

        self.y = 'positive'
        self.x = 'positive'
    
    def move(self):
        if self.x == 'positive':
            new_x = self.xcor() + 0.25
        else:
            new_x = self.xcor() - 0.25
        
        if self.y == 'positive':
            new_y = self.ycor() + 0.25
        else:
            new_y = self.ycor() - 0.25
        self.goto(new_x, new_y)
        self.check_limit()

    def check_limit(self):
        if self.ycor() >= 210:
            self.y = 'negative'
        elif self.ycor() <= -210:
            self.y = 'positive'
