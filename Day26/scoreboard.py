from turtle import Turtle

FONT = ("Segoe UI Black", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super(Scoreboard, self).__init__()
        self.level = 1
        self.highscore = self.readHighscore()
        self.color('white')
        self.ht()
        self.penup()
        self.setpos(x=-240, y=240)
        self.displayScoreboard()


    def displayScoreboard(self):
        self.clear()
        self.write(f"Level: {self.level}    Highscore: {self.highscore} ", font=FONT)

    def increaseScore(self):
        self.level += 1
        self.displayScoreboard()
    
    def displayGameOver(self):
        if self.level > self.highscore:
            self.highscore = self.level
            self.writeHighscore()
        self.goto(-100, 0)
        self.write("GAME OVER", font=FONT)

    def readHighscore(self):
        with open('highscore.txt') as file:
            return int(file.read())


    def writeHighscore(self):
        with open('highscore.txt', mode='w') as file:
            file.write(f"{self.highscore}")