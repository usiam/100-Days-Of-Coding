from turtle import Turtle

ALIGNMENT = 'center'
STYLE = ('Trajan Pro', 30, 'bold')


class ScreenDivider(Turtle):
    def __init__(self):
        super(ScreenDivider, self).__init__()
        self.ht()
        self.penup()
        self.color('white')
        self.displayDivider()

    def displayDivider(self):
        self.goto((0, 335))
        self.right(90)
        self.pensize(5)
        while self.ycor() > -325:
            self.pendown()
            self.fd(10)
            self.penup()
            self.fd(10)

    def writeResult(self, player):
        self.clear()
        self.goto(0, 0)
        self.write(f"   GAME OVER.\n{player} player wins!", align=ALIGNMENT, font=STYLE)
