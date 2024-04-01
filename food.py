from turtle import *
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(0.75,0.75)
        self.color("red")
        self.speed(0)

    def reposition(self):
        x = random.randint(-280,280)
        y = random.randint(-280,280)
        self.goto(x,y)

    def stop(self):
        self.hideturtle()