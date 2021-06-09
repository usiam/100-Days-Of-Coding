from turtle import Turtle,Screen
import random

COLORS = ['red'] * 100
COLORS.append('gold')

class Food(Turtle):

    def __init__(self):
       super().__init__() # we could have also just done self.food = Turtle()
       Screen().tracer(0)
       self.shape('circle')
       self.shapesize(stretch_len = 0.5, stretch_wid = 0.5)
       self.color(random.choice(COLORS))
       self.penup()
       randX, randY = random.randint(-228, 228), random.randint(-228, 228)
       self.setpos(randX, randY)
       Screen().update()

    def newFood(self):
       self.color(random.choice(COLORS))
       randX, randY = random.randint(-228, 228), random.randint(-228, 228)
       self.setpos(randX, randY)

