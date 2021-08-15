from screen import screen, set_screen, draw_edge
from paddle import Paddle

while True:
    # Defines screen size, color and edge line
    set_screen(screen)
    draw_edge()

    # Create player paddles
    right_player = Paddle('right')
    left_player = Paddle('left')

    # Update screen and create a tag for loop
    screen.update()
    playing = True

    screen.listen() # Listen to user input
    # Exit game on Escape keypress
    screen.onkey(screen.bye, 'Escape')
    # Moves right paddle
    screen.onkey(right_player.go_up, 'Up')
    screen.onkey(right_player.go_down, 'Down')
    # Moves left paddle
    screen.onkey(left_player.go_up, 'w')
    screen.onkey(left_player.go_down, 's')

    while playing:
        try:
            screen.update()
        
        except:
            break
