import random

class Animal:

    def __init__(self):
        self.eyes = 2

    def breath(self):
        print("Inhale, exhale.")

class Fish(Animal): # a good way to remember this is that a fish is a function of animal

    def __init__(self):
        super().__init__() #initialize the super class every tine the fish class gets initialized
        self.fins = 2

    def swim(self):
        print(f"Can swim with their {self.fins} fins")

    def breath(self):
        super().breath()
        print("underwater.")
# But a fish can also breath and it also has eyes like all animals so we inherit those from animal class

dory = Fish()
print(dory.eyes)
dory.breath()
dory.swim()