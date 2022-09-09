from turtle import Turtle, Screen

timi = Turtle()
screen = Screen()


def move_forward():
    timi.forward(10)


def move_backward():
    timi.back(10)


def turn_right():
    timi.right(10)


def turn_left():
    timi.left(10)


def clear():
    timi.clear()
    timi.penup()
    timi.home()
    timi.pendown()


screen.listen()
screen.onkey(fun=move_forward, key="w")
screen.onkey(fun=move_backward, key="s")
screen.onkey(fun=turn_left, key="a")
screen.onkey(fun=turn_right, key="d")
screen.onkey(fun=clear, key="c")
screen.exitonclick()
