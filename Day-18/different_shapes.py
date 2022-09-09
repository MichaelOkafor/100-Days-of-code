from turtle import Turtle, Screen
import random
timi = Turtle()

timi.shape("turtle")
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGrey",
           "SeaGreen"]


def draw_shape(num_of_sides):
    angle = 360 / num_of_sides
    for _ in range(num_of_sides):
        timi.forward(100)
        timi.right(angle)


for shapes in range(3, 11):
    timi.color(random.choice(colours))
    draw_shape(shapes)

screen = Screen()
screen.exitonclick()
