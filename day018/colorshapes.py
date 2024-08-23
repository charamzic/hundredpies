import random
from turtle import Screen, Turtle

tim = Turtle()
tim.shape("turtle")

colors = [
    "deep pink",
    "yellow green",
    "dodger blue",
    "orange red",
    "medium purple",
    "navajo white",
    "olive drab",
    "light sky blue",
    "violet",
    "gold",
]


def draw(sides):
    angle = 360 / sides
    for _ in range(sides):
        tim.forward(100)
        tim.right(angle)


screen = Screen()

for shape_side_n in range(3, 11):
    tim.color(random.choice(colors))
    draw(shape_side_n)

screen.exitonclick()
