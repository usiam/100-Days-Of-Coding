from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 2
MOVE_INCREMENT = 2


class CarManager():
    def __init__(self):
        self.carArr = []
        self.createCar()
        self.moveDistance = STARTING_MOVE_DISTANCE

    def moveCars(self):
        '''
        Moves all the cars in the carArr array of cars
        '''
        for car in self.carArr:
            car.fd(self.moveDistance)
    
    def createCar(self):
        '''
        creates a car turtle object and appends it to the carrArr array
        '''
        if random.randint(1,14) == 1:
            car = Turtle()
            car.penup()
            car.shape('square')
            car.color(random.choice(COLORS))
            car.shapesize(stretch_len=1.5)
            car.setheading(180)
            car.goto(300, random.randint(-240, 240))
            self.carArr.append(car)

    def increaseSpeed(self):
        self.moveDistance += MOVE_INCREMENT