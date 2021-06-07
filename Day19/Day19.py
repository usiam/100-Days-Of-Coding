"""
Created on Thu Jun  7 12:15:26 2021

@author: Tahamid
"""

import random
import turtle
from turtle import Turtle, Screen

# Key listeners

tim = Turtle()
screen = Screen()
turtle.screensize(screen.window_width(), screen.window_height())
screen.colormode(255)
tim.color('DarkGreen')
tim.pensize(5)
screen.listen()


def moveFd():
    tim.fd(10)


def moveBk():
    tim.bk(10)


def turnRight():
    tim.setheading(tim.heading() - 10)


def turnLeft():
    tim.setheading(tim.heading() + 10)


def setColor():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


def changePenColor():
    color = setColor()
    tim.color(color)


def drawDot(x, y):
    color = setColor()
    tim.dot(10, color)


def turtleVisibility():
    if tim.isvisible():
        tim.ht()
    else:
        tim.st()


def clearScreen():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


def currHeading():
    tim.setheading(tim.heading())


screen.onkeypress(moveFd, 'w')

screen.onkeypress(moveBk, 's')

screen.onkeypress(turnLeft, 'a')
screen.onkeyrelease(currHeading, 'a')

screen.onkeypress(turnRight, 'd')
screen.onkeyrelease(currHeading, 'd')

screen.onkey(changePenColor, 'space')

screen.onkey(setColor, 'r')

screen.onkey(turtleVisibility, 'z')

screen.onkey(clearScreen, 'c')

screen.onclick(drawDot)

screen.mainloop()
