from turtle import Turtle, Screen
import random

# import colorgram
#
# colors = colorgram.extract('download.jpeg',25)
#
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

tim = Turtle()
screen = Screen()
tim.hideturtle()
tim.speed("fastest")
screen.colormode(255)
color_list = [(245, 225, 230), (215, 162, 94), (238, 212, 90), (216, 123, 166), (167, 77, 44), (208, 220, 231),
              (116, 174, 221), (209, 225, 212), (212, 85, 133), (61, 127, 61), (68, 43, 37), (240, 168, 190),
              (72, 107, 211), (160, 57, 106), (229, 83, 63), (68, 85, 142), (80, 166, 66), (128, 191, 167),
              (34, 86, 40), (129, 43, 33), (164, 195, 45), (214, 181, 175), (170, 207, 186), (181, 27, 57)]

# MyCode


screen.setworldcoordinates(-1, -1, screen.window_width() - 1, screen.window_height() - 1)
tim.hideturtle()
tim.speed("fastest")


def horizontal_move():
    for x in range(10):
        tim.pencolor(random.choice(color_list))
        tim.dot(20)
        tim.penup()
        tim.forward(50)


y_coordinate = 0  # Introduce variable

def next_line():
        global y_coordinate  # Gain access to global variable
        y_coordinate += 50  # Increment the y-coordinate by 50 each call
        tim.goto(0, y_coordinate)  # Move the turtle to the next line

for _ in range(10):
    horizontal_move()
    next_line()


# Angela Yu Code

# tim.penup()
# tim.setheading(225)
# tim.forward(300)
# tim.setheading(0)
# number_of_dots = 100
#
#
# for dot_count in range(1, number_of_dots + 1):
#     tim.dot(20, random.choice(color_list))
#     tim.forward(50)
#
#     if dot_count % 10 == 0:
#         tim.setheading(90)
#         tim.forward(50)
#         tim.setheading(180)
#         tim.forward(500)
#         tim.setheading(0)

screen.exitonclick()

