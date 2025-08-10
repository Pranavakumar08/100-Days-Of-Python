import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

sb = ScoreBoard()
pl = Player()
cm = CarManager()

screen.listen()
screen.onkey(pl.move,"Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    cm.create_car()
    cm.move()

    if pl.if_won():
        sb.update_level()
        pl.reset_position()
        cm.update_speed()

    for car in cm.cars_list:
        if car.distance(pl) < 20 :
            game_is_on = False
            sb.game_over()

screen.exitonclick()