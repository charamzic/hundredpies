import random
from turtle import Screen, Turtle

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(
    title="Make your bet!", prompt="Which turtle will win the race? Enter a color: "
)
colors = ["red", "blue", "orange", "violet"]
turtle_racers = []

for i in range(0, 4):
    turt = Turtle(shape="turtle")
    turt.color(colors[i])
    turt.penup()
    turt.goto(x=-230, y=i * 30)
    turtle_racers.append(turt)


if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtle_racers:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)


screen.exitonclick()
