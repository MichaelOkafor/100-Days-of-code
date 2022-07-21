from turtle import Turtle, Screen

timi_the_turtle = Turtle()
timi_the_turtle.shape("turtle")
timi_the_turtle.color("brown")

for _ in range(4):
    timi_the_turtle.fd(100)
    timi_the_turtle.lt(90)

screen = Screen()
screen.exitonclick()