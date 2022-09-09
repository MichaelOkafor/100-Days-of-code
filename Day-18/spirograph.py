import turtle as t
import random

timi = t.Turtle()
timi.shape("turtle")
t.colormode(255)


def random_colour():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colour = (r, g, b)
    return colour


timi.speed("fastest")


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        timi.color(random_colour())
        timi.circle(100)
        current_heading = timi.heading()
        timi.setheading(current_heading - size_of_gap)


draw_spirograph(5)

screen = t.Screen()
screen.exitonclick()
