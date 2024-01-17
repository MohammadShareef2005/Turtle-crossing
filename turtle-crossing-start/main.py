import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
score = Scoreboard()
car = CarManager()
screen.setup(width=600, height=600)
screen.title("Turtle Game")
screen.tracer(0)
screen.listen()
play = Player()
screen.onkey(play.up, "Up")
game_is_on = True
while game_is_on:
    time.sleep(score.spe)
    screen.update()
    car.create_car()
    car.move()
    for i in car.all_cars:

        if i.distance(play) < 20:
            score.game_over()
            game_is_on = False

    if play.ycor() > 280:
        play.restart()
        score.score_inc()

screen.exitonclick()
