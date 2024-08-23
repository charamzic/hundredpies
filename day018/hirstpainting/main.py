import random
import turtle as t

# import colorgram

# rgb_colors = []
# colors = colorgram.extract("dots.jpg", 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_colors.append((r, g, b))

t.colormode(255)
tim = t.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()

color_list = [
    (59, 95, 137),
    (103, 166, 198),
    (177, 165, 120),
    (229, 235, 233),
    (225, 201, 95),
    (27, 161, 193),
    (76, 130, 186),
    (65, 50, 42),
    (51, 58, 67),
    (160, 71, 50),
    (150, 209, 219),
    (193, 8, 19),
    (207, 184, 37),
    (54, 62, 77),
    (7, 146, 124),
    (216, 99, 51),
    (208, 29, 38),
    (147, 168, 161),
    (165, 212, 207),
    (42, 164, 136),
    (177, 150, 154),
    (173, 18, 15),
    (53, 62, 58),
    (67, 64, 57),
    (172, 192, 215),
    (5, 90, 51),
    (43, 27, 29),
]

screen = t.Screen()

tim.setheading(255)
tim.forward(300)
tim.setheading(0)
dots_amount = 100

for dot_count in range(1, dots_amount + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen.exitonclick()
