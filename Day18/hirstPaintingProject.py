"""
Created on Sun Jun  6 23:48:43 2021

@author: Tahamid
"""

import turtle
from turtle import Turtle, Screen
import random

# import colorgram
#
# rgbColors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r, g, b = color.rgb
#     rgbTuple = (r, g, b)
#     rgbColors.append(rgbTuple)

colors = [(202, 164, 110), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

# 10 x 10
# radius = 20
# gap = 50

tim = Turtle()
screen = Screen()
turtle.colormode(255)
tim.speed('fastest')
screen.title("Polka Dots")
x = - screen.canvwidth/2
y = - screen.canvheight/2 - 75
tim.penup()
tim.setpos((x,y))
for _ in range(10):
    for _ in range(10):
        color = random.choice(colors)
        tim.pendown()
        tim.dot(10, color)
        tim.penup()
        tim.fd(50)
    tim.penup()
    tim.setpos((x, tim.pos()[1] + 50))
tim.ht()

turtle.screensize(screen.window_width(), screen.window_height())
screen.exitonclick()