def hurdle():
    move()
    turn_left()
    move()
    turn_right()
    move()

def turn_right():
    turn_left()
    turn_left()
    turn_left()

while not at_goal():
    if wall_in_front():
        hurdle()
    else:
        move()
