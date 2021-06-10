import random
from turtle import Turtle

SPEED = 0.03


class Puck(Turtle):
    def __init__(self):
        super(Puck, self).__init__()
        self.penup()
        self.color('white')
        self.shape('square')
        self.dx = random.choice([-10, 10])
        self.dy = random.choice([-10, 10])
        self.puckSpeed = SPEED

    def move(self):
        x = self.xcor() + self.dx
        y = self.ycor() + self.dy
        self.goto(x, y)

    def changeDY(self):
        self.dy *= -1

    def changeDX(self):
        self.dx *= -1

    def softReset(self):
        self.goto(0, 0)
        self.changeDX()
        self.puckSpeed = SPEED

    def speedUp(self):
        self.puckSpeed *= 0.95  # decreases the time.sleep() value and hence increases the speed
