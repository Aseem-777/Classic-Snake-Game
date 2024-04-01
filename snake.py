import turtle
import time

screen = turtle.Screen()
screen.setup(600,600)
screen.bgcolor('black')
screen.title('Classic snake game')
screen.tracer(0)

class Snake:
    def __init__(self):
        self.segments = []
        self.segment_pos = [(0,0),(-20,0),(-40,0)]
        self.direction = 'right'

    def create(self):
        for pos in self.segment_pos:
            self.add_segment(pos)

    def add_segment(self, pos):
        snake_segment = turtle.Turtle('square')
        snake_segment.penup()
        snake_segment.color('white')
        snake_segment.goto(pos)
        self.segments.append(snake_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for segment in range(len(self.segments)-1,0,-1):
            x = self.segments[segment-1].xcor()
            y = self.segments[segment-1].ycor()
            self.segments[segment].goto(x,y)
        self.segments[0].forward(20)
        screen.update()
        time.sleep(0.1)

    def dir_right(self):
        if self.direction != 'left':
            self.segments[0].setheading(0)
            self.direction = 'right'
        else:
            pass

    def dir_left(self):
        if self.direction != 'right':
            self.segments[0].setheading(180)
            self.direction = 'left'
        else:
            pass

    def dir_forward(self):
        if self.direction != 'back':
            self.segments[0].setheading(90)
            self.direction = 'forward'
        else:
            pass

    def dir_back(self):
        if self.direction != 'forward':
            self.segments[0].setheading(270)
            self.direction = 'back'
        else:
            pass


    def stop(self):
        for self.segment in self.segments:
            self.segment.hideturtle()

    def reset(self):
        for segment in self.segments:
            segment.goto(1000,1000)
        self.segments.clear()
        self.create()
