from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.spe = 0.1
        self.score_bor()

    def score_bor(self):
        self.clear()
        self.goto(-280, 250)
        self.write(f"Score = {self.score}", align="left", font=FONT)

    def score_inc(self):
        self.score += 1
        self.spe *= 0.9
        self.score_bor()

    def game_over(self):
        self.penup()
        self.goto(0, 0)
        self.hideturtle()
        self.write("Game Over", font=FONT, align="center")
