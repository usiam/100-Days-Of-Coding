"""
Created on Tue Jun 8 2:15:26 2021

@author: Tahamid
"""

import time
from turtle import Screen

from food import Food
from scoreboard import Scoreboard
from snake import Snake

screen = Screen()
screen.setup(width=500, height=500)
screen.bgcolor('black')
screen.tracer(0)  # turns off auto update so now we have to manually update using screen.update()
screen.title('Snake Game')

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.moveUp, "Up")
screen.onkey(snake.moveDown, "Down")
screen.onkey(snake.moveLeft, "Left")
screen.onkey(snake.moveRight, "Right")

gameOver = False
while not gameOver:
    screen.update()  # screen updates every time each segment moves
    time.sleep(0.07)  # n second delay before next update
    snake.move()

    # Collision detection with food
    if snake.head.distance(food) < 15:
        snake.grow()
        scoreboard.increaseScore(food.pencolor())
        food.newFood()

    # Collision detection with wall
    if snake.head.xcor() > 245 or snake.head.xcor() < -245 or snake.head.ycor() > 245 or snake.head.ycor() < - 245:
        scoreboard.resetScore()
        snake.reset()

    # Collision detection with self
    for seg in snake.snakeBody[1:]:
        if snake.head.distance(seg) < 10:
            scoreboard.resetScore()
            snake.reset()

screen.mainloop()
