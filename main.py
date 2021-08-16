from screen import screen, set_screen, draw_edge
from paddle import Paddle
from ball import Ball

while True:
    # Defines screen size, color and edge line
    set_screen(screen)
    draw_edge()

    # Create player paddles
    r_player = Paddle('right')
    l_player = Paddle('left')
    ball = Ball()


    # Update screen and create a tag for loop
    screen.update()
    playing = True

    screen.listen() # Listen to user input
    # Exit game on Escape keypress
    screen.onkey(screen.bye, 'Escape')
    # Moves right paddle
    screen.onkey(r_player.go_up, 'Up')
    screen.onkey(r_player.go_down, 'Down')
    # Moves left paddle
    screen.onkey(l_player.go_up, 'w')
    screen.onkey(l_player.go_down, 's')


    while playing:
        try:
            screen.update()
            
            ball.move()

            if (ball.xcor() >= 340) and (r_player.distance(ball) <= 45):
                ball.paddle_colide()
            elif (ball.xcor() >= 370):
                ball.refresh()
                
            elif (ball.xcor() <= -340) and (l_player.distance(ball) <= 45):
                ball.paddle_colide()
            elif (ball.xcor() <= -370):
                ball.refresh()
            
            screen.update()

        except:
            raise
