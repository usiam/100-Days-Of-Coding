"""
Created on Thu Jun  7 2:15:26 2021

@author: Tahamid
"""
import random
from turtle import Turtle, Screen
import turtle

# setting up the canvas
screen = Screen()
screen.tracer(0)
screen.bgpic('racetrack.png')
width = 500
height = 400
screen.setup(width, height)

# initial positions for the turtles
startX = - 240
startY = - 120

# building the turtles
colors = ['red', 'green', 'blue', 'black', 'orange', 'purple']

writer = Turtle()
writer.penup()
writer.ht()
writer.setpos(x = 0, y = 180)
writer.write(f"Today's turtles are: {', '.join(colors)}", move=False, align="center", font=("Arial", 12, "bold"))

screen.update()
turtles = {}
for i in range(6):
    turtle = Turtle(shape='turtle')
    turtle.speed(7)
    color = colors[i]
    turtle.color(color)
    turtle.penup()
    turtle.goto(startX, startY)
    startY += 45  # makes sure the turtles are evenly spaced
    turtles[turtle] = color  # the key is the turtle object and the values are the colors
screen.update()
turtleWidth = 40  # each turtle obj is 40 px in width
endLine = width / 2 - turtleWidth / 2  # this defines the position where the race ends
screen.tracer(1)
raceOn = False
# starts the race
usrTurtleCol = screen.textinput(title="Make your bet.", prompt='Choose your turtle by entering its color: ')
if usrTurtleCol:
    raceOn = True
while raceOn:
    for turtle in turtles:
        if turtle.xcor() >= endLine:
            raceOn = False
            winningCol = turtle.pencolor()
            if winningCol == usrTurtleCol.lower():
                print(f"You win. {winningCol.title()} turtle won!")
            else:
                print(f"You lost. {winningCol.title()} turtle won!")
        else:
            goFdDist = random.randint(0, 10)
            turtle.fd(goFdDist)

screen.mainloop()
