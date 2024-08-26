import time
import turtle

from car_manager import CarManager
from player import Player
from scoreboard import Scoreboard

scr = turtle.Screen()
scr.setup(width=600, height=600)
scr.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

scr.listen()
scr.onkey(player.go_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    scr.update()

    car_manager.create_car()
    car_manager.move_cars()

    # Car collision
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    # Successfull crossing
    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()

scr.exitonclick()
turtle.done()
