import turtle
from turtle import Turtle

POSITIONS = [(0,0), (-20, 0), (-40, 0)]
MOVEDIST = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.snakeBody = [] # we will be using the snakeBody in all our methods so we just make the list at instantiation
        self.createBody()
        self.head = self.snakeBody[0]

    def createBody(self):
        for position in POSITIONS:
            self.addSeg(position)


    def move(self):
        for i in range(len(self.snakeBody) - 1, 0, -1):  # generates 2, 1
            self.snakeBody[i].setpos(self.snakeBody[i - 1].pos())
        self.head.fd(MOVEDIST)

    def moveUp(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def moveDown(self):
        if self.head.heading() != UP:
            self.head.setheading(270)

    def moveRight(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)

    def moveLeft(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)

    def grow(self):
        self.addSeg(self.snakeBody[-1].pos())

    def addSeg(self, position):
        snkSegment = Turtle(shape='square')
        snkSegment.penup()
        snkSegment.color('white')
        snkSegment.setpos(position)
        self.snakeBody.append(snkSegment)