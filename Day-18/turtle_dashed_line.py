from turtle import Turtle, Screen

timi = Turtle()

timi.shape("turtle")

for _ in range(15):
    timi.forward(10)
    timi.penup()
    timi.forward(10)
    timi.pendown()

screen = Screen()
screen.exitonclick()
