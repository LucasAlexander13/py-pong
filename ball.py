from turtle import Turtle
from random import choice

color = [
    'orange', 
    'dark orange', 
    'firebrick', 
    'dark red', 
    'crimson', 
    'medium violet red', 
    'dark magenta', 
    'medium orchid', 
    'medium purple', 
    'indigo', 
    'slate blue',
    ]

class Ball(Turtle):
    def __init__(self,):
        super().__init__()
        # Defines paddle attributes
        self.shape('square')
        self.shapesize(stretch_wid=0.8)
        self.color('white')
        self.penup()
        self.set_direction()
    
    def set_direction(self):
        self.x = choice(('positive', 'negative'))
        self.y = choice(('positive', 'negative'))
    
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
            self.pick_color()

        elif self.ycor() <= -210:
            self.y = 'positive'
            self.pick_color()
    
    def pick_color(self):
        self.color(choice(color))
