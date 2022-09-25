from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)  # This is to turn off the animation

paddle = Turtle()
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=5, stretch_len=1)  # the original turtle length & width is 20:20
paddle.penup()
paddle.goto(x=350, y=0)


def go_up():
    new_y = paddle.ycor() + 20
    paddle.goto(x=paddle.xcor(), y=new_y)


def go_down():
    new_y = paddle.ycor() - 20
    paddle.goto(x=paddle.xcor(), y=new_y)


screen.listen()
screen.onkey(go_up, "up")
screen.onkey(go_down, "down")

game_is_on = True
while game_is_on:
    screen.update()  # this is to update the screen after turning off the animation

screen.exitonclick()
