from turtle import Screen, Turtle

screen = Screen()

def set_screen(screen):
    # set main screen proprieties
    screen.screensize(800, 500) 
    screen.bgcolor('black')
    screen.title('PyPong')
    screen.tracer(0)

def draw_edge():
    # start the turtle on the right top corner
    board = Turtle()
    board.penup()
    board.color('firebrick')
    board.goto(380, 220)

    # draw the edge line of the game
    board.pendown()
    board.goto(380, -220)
    board.goto(-380, -220)
    board.goto(-380, 220)
    board.goto(380, 220)
    board.hideturtle()
