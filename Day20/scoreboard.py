from turtle import Turtle

ALIGNMENT, FONT = "center", ("Courier", 14, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = self.readHighscore()
        self.color('white')
        self.ht()
        self.penup()
        self.setpos(x=0, y=230)
        self.displayScoreboard()

    def displayScoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}    Highscore: {self.highscore}", align=ALIGNMENT, font=FONT)

    def increaseScore(self, color):
        if color == 'red':
            self.score += 1
        elif color == 'gold':
            self.score += 10
        self.displayScoreboard()

    def resetScore(self):
        if self.score > self.highscore:
            self.highscore = self.score
        self.writeHighscore()
        self.score = 0
        self.displayScoreboard()

    # def gameOver(self):
    #     self.setpos(0, 0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def writeHighscore(self):
        with open('highscore.txt', mode = 'w') as file:
            file.write(f"{self.highscore}")

    def readHighscore(self):
        with open('highscore.txt') as file:
            content = file.read()
        return int(content)