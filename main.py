from screen import screen, set_screen, draw_edge
from paddle import Paddle
from score import Score
from ball import Ball

while True:
    # Defines screen size, color and edge line
    set_screen(screen)
    draw_edge()

    # Create player paddles
    r_player = Paddle('right')
    l_player = Paddle('left')
    score = Score()
    ball = Ball()


    # Update screen and create a tag for loop
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
            score.draw_score()
            screen.update()

            ball.move()

            if ball.xcor() <= -340 and ball.distance(l_player) < 70:
                if not(ball.xcor() <= -345):
                    ball.paddle_colide()
            elif (ball.xcor() <= -370):

                score.score[1] += 1
                if score.score[1] == 5:
                    score.game_over("Player 1")
                else:
                    ball.refresh()

            if ball.xcor() >= 340 and ball.distance(r_player) < 70:
                if not(ball.xcor() >= 345):
                    ball.paddle_colide()
            elif (ball.xcor() >= 370):

                score.score[0] += 1
                if score.score[0] == 5:
                    score.game_over("Player 2")
                else:
                    ball.refresh()
                


        except:
            raise
