from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(x=0, y=260)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.write(f"Score: {self.score}", align="center", font=("courier", 20, "normal"))

    def game_over(self):
        self.goto(x=0, y=0)
        self.write("GAME OVER", align="center", font=("courier", 20, "normal"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()
