from turtle import Turtle

UP = 90
DOWN = 270


class Paddle(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.x, self.y = x, y
        self.color('white')
        self.penup()
        self.shape('square')
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.setheading(UP)
        self.goto(x, y)

    def up(self):
        self.setheading(UP)
        self.fd(15)

    def down(self):
        self.setheading(DOWN)
        self.fd(15)
