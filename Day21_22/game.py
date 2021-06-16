"""
Created on Wed Jun 9, 10 12:15:26 2021

@author: Tahamid
"""
import time
from turtle import Screen

from paddle import Paddle
from puck import Puck
from scoreboard import Scoreboard
from screenDivider import ScreenDivider

HEIGHT = 700
WIDTH = 1200
PADDLEXPOS = 550
YBOUND = HEIGHT / 2 - 15
XBOUND = WIDTH / 2

if __name__ == '__main__':

    screen = Screen()
    screen.setup(width=WIDTH, height=HEIGHT)
    screen.bgcolor('black')
    screen.tracer(0)
    screen.title("PONG")

    rScoreboard = Scoreboard((55, 270))
    lScoreboard = Scoreboard((-55, 270))
    screenDivider = ScreenDivider()
    puck = Puck()
    rPaddle = Paddle(PADDLEXPOS, 0)
    lPaddle = Paddle(- PADDLEXPOS, 0)

    maxScore = int(screen.textinput(title="", prompt='Choose the maximum score needed to win: '))

    if maxScore:
        gameOver = False

    screen.listen()

    screen.onkeypress(rPaddle.up, 'Up')
    screen.onkeypress(rPaddle.down, 'Down')

    screen.onkeypress(lPaddle.up, 'w')
    screen.onkeypress(lPaddle.down, 's')
    while not gameOver:
        time.sleep(puck.puckSpeed)
        screen.update()
        puck.move()

        # Detect collision of puck and upper or lower walls
        if puck.ycor() > YBOUND or puck.ycor() < - YBOUND:
            puck.changeDY()

        # Detect collision of puck and paddle
        elif (puck.distance(rPaddle) < 50 and puck.xcor() > PADDLEXPOS - 20) or (
                puck.distance(lPaddle) < 50 and puck.xcor() < - PADDLEXPOS + 20):
            puck.changeDX()
            puck.speedUp()

        # Detect collision of puck and left/right walls
        elif puck.xcor() > XBOUND:
            lScoreboard.increaseScore()
            puck.softReset()
        elif puck.xcor() < - XBOUND:
            rScoreboard.increaseScore()
            puck.softReset()

        if rScoreboard.score == maxScore:
            screenDivider.writeResult('Right')
            gameOver = True
        elif lScoreboard.score == maxScore:
            screenDivider.writeResult('Left')
            gameOver = True

    screen.mainloop()
