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

for step in range(6):
    hurdle()

# OR
number_of_hurdles = 6
while number_of_hurdles > 0:
    hurdle()
    number_of_hurdles -= 1
    print(number_of_hurdles)