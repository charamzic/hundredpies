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


SCREEN = t.Screen()
tim.speed("fastest")


def draw_spriograph(gap_size):
    for _ in range(int(360 / gap_size)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + gap_size)


draw_spriograph(5)


SCREEN.exitonclick()
