from turtle import Turtle

ALIGNMENT, FONT = "center", ("Courier", 14, "bold")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.ht()
        self.penup()
        self.setpos(x = 0, y = 230)
        self.updateScoreboard()

    def updateScoreboard(self):
        self.write(f"Score: {self.score}", align = ALIGNMENT, font = FONT)

    def increaseScore(self, color):
        if color == 'red':
            self.score += 1
        elif color == 'gold':
            self.score += 10
        self.clear()
        self.updateScoreboard()

    def gameOver(self):
        self.setpos(0, 0)
        self.write("GAME OVER", align = ALIGNMENT, font = FONT)