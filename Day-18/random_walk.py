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


directions = [0, 90, 180, 270]
timi.pensize(10)
timi.speed("fastest")

for _ in range(200):
    timi.color(random_colour())
    timi.forward(30)
    timi.setheading(random.choice(directions))
