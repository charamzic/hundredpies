from turtle import Screen
from cobra import Cobra
import time
import sys

from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Cobra")
screen.tracer(0)

segments = []

cobra = Cobra()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(cobra.up, "Up")
screen.onkey(cobra.down, "Down")
screen.onkey(cobra.left, "Left")
screen.onkey(cobra.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    cobra.move()

    # Food collision
    if cobra.head.distance(food) < 15:
        food.refresh()
        cobra.extend()
        scoreboard.increase_score()

    # Walls collision
    if cobra.head.xcor() > 280 or cobra.head.xcor() < -280 or cobra.head.ycor() > 280 or cobra.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    # Body collision
    for segment in cobra.segments[1:]:
        if cobra.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()
