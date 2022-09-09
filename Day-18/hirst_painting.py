import colorgram 
import turtle as t
import random

t.colormode(255)
timi = t.Turtle()
timi.speed("fastest")
timi.penup()
timi.hideturtle()

rgb_colours = []
colours = colorgram.extract("image.jpg", 9)

for colour in colours:
    r = colour.rgb.r
    g = colour.rgb.g
    b = colour.rgb.b
    new_colour = (r, g, b)
    rgb_colours.append(new_colour)

print(rgb_colours)

colour_list = rgb_colours

timi.setheading(225)
timi.forward(250)
timi.setheading(0)
num_of_dots = 100

for dot_count in range(1, num_of_dots + 1):
    timi.dot(20, random.choice(colour_list))
    timi.forward(50)

    if dot_count % 10 == 0:
        timi.setheading(90)
        timi.forward(50)
        timi.setheading(180)
        timi.forward(500)
        timi.setheading(0)

screen = t.Screen()
screen.exitonclick()
