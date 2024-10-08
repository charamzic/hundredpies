from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.color("pink")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        self.goto(
            random.randint(-280, 280),
            random.randint(-280, 280)
        )
