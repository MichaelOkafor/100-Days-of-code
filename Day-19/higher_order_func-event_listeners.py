from turtle import Turtle, Screen

timi = Turtle()
screen = Screen()


def move_forward():
    timi.forward(10)


screen.listen()
screen.onkey(key="space", fun=move_forward)
screen.exitonclick()
