import random
import turtle as t

tim = t.Turtle()
tim.shape("turtle")
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


directions = [0, 90, 180, 270]
tim.pensize(12)
tim.speed("fastest")

screen = t.Screen()

for _ in range(400):
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(directions))

screen.exitonclick()
