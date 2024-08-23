from turtle import Screen, Turtle

tim = Turtle()
screen = Screen()


def move_forward():
    tim.forward(10)


def move_backwards():
    tim.backward(10)


def move_right():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)


def move_left():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)


def clear():
    tim.home()
    tim.clear()


screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=move_left)
screen.onkey(key="d", fun=move_right)
screen.onkey(key="c", fun=clear)
screen.exitonclick()
