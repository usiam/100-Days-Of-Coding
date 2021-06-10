from turtle import Turtle

ALIGNMENT = 'center'
STYLE = ('Trajan Pro', 45, 'bold')


class Scoreboard(Turtle):
    def __init__(self, position):
        super(Scoreboard, self).__init__()
        self.score = 0
        self.position = position
        self.ht()
        self.penup()
        self.color('white')
        self.displayScore(position)

    def displayScore(self, position):
        self.goto(position)
        self.write(f"{self.score}", align=ALIGNMENT, font=STYLE)

    def increaseScore(self):
        self.score += 1
        self.clear()
        self.displayScore(self.position)
