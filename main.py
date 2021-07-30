import turtle as turtle_module
import random

turtle_module.colormode(255)
tim = turtle_module.Turtle()
color_list = [(189, 58, 25), (22, 29, 69), (49, 33, 18), (244, 234, 72), (243, 250, 247), (147, 23, 37), (153, 21, 14), (56, 28, 39), (218, 142, 80), (108, 165, 224), (249, 240, 244), (204, 74, 124), (26, 43, 124), (43, 81, 152), (24, 48, 31), (57, 110, 55), (89, 100, 204), (215, 86, 55), (228, 129, 20), (41, 83, 51), (250, 226, 2), (140, 187, 173), (154, 58, 72), (87, 166, 60), (148, 208, 226), (151, 189, 238), (150, 224, 215), (68, 72, 24)]
tim.penup()
tim.hideturtle()
tim.setheading(225)
tim.forward(350)
tim.setheading(0)
tim.speed("fastest")


number_of_dots= 101

for count_dot in range(1, number_of_dots):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)
    if count_dot % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


screen = turtle_module.Screen()
screen.exitonclick()

