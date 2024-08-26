from turtle import Screen
from cobra import Cobra
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Cobra")
screen.tracer(0)


segments = []

cobra = Cobra()

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

screen.exitonclick()
