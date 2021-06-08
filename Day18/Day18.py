"""
Created on Sun Jun  6 23:48:43 2021

@author: Tahamid
"""

import random
import turtle
from turtle import Turtle, Screen
from os import system, name


clear = lambda : system('cls' if name == 'nt' else 'clear')

def randomColor():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    randColor = (r,g,b)
    return randColor

def drawDashedLine():
    tim.pensize(7)
    color = randomColor()
    tim.color(color)
    for i in range(15):
        tim.fd(10)
        tim.penup()
        tim.fd(10)
        tim.pendown()

def drawShape(sides):
    tim.pensize(10)
    color = randomColor()
    tim.color(color)
    rot = 360/sides
    for i in range(sides):
        tim.fd(70)
        tim.right(rot)

def drawNSidedShapes(N):
    tim.pensize(5)
    sides = range(3, N)
    for side in sides:
        color = randomColor()
        tim.color(color)
        drawShape(side)

def randomWalk():
    tim.pensize(10)
    tim.speed(9)
    for _ in range(100):
        color = randomColor()
        tim.color(color)
        randPace = random.randint(20, 40)
        tim.fd(randPace)
        angles = [0, 90, 180, 270]
        randAngle = random.choice(angles)
        tim.setheading(randAngle)

def spirograph(gapAngle):
    tim.pensize(2)
    tim.speed('fastest')
    for _ in range(int(360 / gapAngle)):
        color = randomColor()
        tim.color(color)
        tim.circle(100)
        tim.setheading(tim.heading() + gapAngle) # sets the heading to be the curr heading + however much angular
                                                    # gap the user wants between circles

def makeCircularPatters(nPatterns):
    screen.tracer(0)
    for n in range(nPatterns):
        tim.speed(5)
        tim.penup()
        x, y = random.randint(-400, 400), random.randint(-400, 400)
        randPos = (x,y)
        tim.goto(randPos)
        tim.pendown()

        color = randomColor()
        tim.color(color)

        circleSize = random.randint(10, 40)
        tim.pensize(random.randint(1, 5))

        for i in range(6):
            tim.circle(circleSize)
            tim.left(60)
            screen.update()

clear()
print("Welcome to the basic turtle program!\n")
print("Here are the things this program can draw for now: 1. N sided polygons, 2. All polygons upto your N Sided polygon, "
      "3. Dashed line, 4. Random walk, 5. Spirograph, 6. Circular patterns\n")
func = input("What do you want it to do? Choose any between 1-6: ")

turtle.colormode(255)
tim = Turtle()
screen = Screen()
screen.bgcolor('black')
turtle.screensize(screen.window_width(), screen.window_height())

if func == '1':
    side = int(input("How many sides does your polygon have? "))
    screen.title('N sided Polygon')
    drawShape(side)
elif func == '2':
    maxSide = int(input("What is the maximum sided polygon you want? "))
    screen.title('Multiple polygons')
    drawNSidedShapes(maxSide)
elif func == '3':
    screen.title('Dashed line')
    drawDashedLine()
elif func == '4':
    screen.title('Random walk')
    randomWalk()
elif func == '5':
    gap = float(input("How much angular gap do you want between each circle? "))
    screen.title('Spirograph')
    spirograph(gap)
elif func == '6':
    num = int(input("How many patterns do you want? "))
    screen.title('Circular patterns')
    makeCircularPatters(num)

# 169. Tuples
# (a, b, c)

# myTuple = (1, 2, 3)
# print(myTuple[0]) # prints 1

# unlike the elements in a list a tuple's elements are fixed you can only read it not write/assign i.e. it is immutable
# myTuple[0] = 4 will give you an error.
# you can convert your tuple into a list using list(myTuple)



screen.mainloop()