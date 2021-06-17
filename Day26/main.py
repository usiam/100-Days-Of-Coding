import time
from turtle import Screen
from player import Player
from carManager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor('black')
player = Player()
carManager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(player.up, 'w')
screen.onkeypress(player.left, 'a')
screen.onkeypress(player.right, 'd')

game_is_on = True

while game_is_on:
    time.sleep(0.008)
    screen.update()
    carManager.createCar()
    carManager.moveCars()

    if player.reachedFinishLine():
        player.goToStart()
        scoreboard.increaseScore()
        carManager.increaseSpeed()

    for car in carManager.carArr:
         if player.distance(car) <= 22:
             game_is_on = False


scoreboard.displayGameOver()
screen.mainloop()