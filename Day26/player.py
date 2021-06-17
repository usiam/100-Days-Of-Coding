from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.color('white')
        self.penup()
        self.setheading(90)
        self.goToStart()

    def up(self):
        self.fd(MOVE_DISTANCE)

    def left(self):
        self.setheading(180)
        self.fd(10)
        self.setheading(90)

    def right(self):
        self.setheading(0)
        self.fd(10)
        self.setheading(90)

    def goToStart(self):
            self.goto(STARTING_POSITION)

    def reachedFinishLine(self):
        if self.ycor() >= FINISH_LINE_Y:
            return True
        else:
            return False