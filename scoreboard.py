from turtle import *

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.color('white')
        with open('Classic Snake Game/data.txt', 'r') as f:
            hs = int(f.read())
            self.highscore = hs
            f.close()
        self.goto(0,240)
        self.write(f"Score: {self.score}    High score: {self.highscore}",align="center",font=('Arial',14,'normal'))
        

    def increase_score(self):
        self.score += 1
        self.update_score()

    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.color('red')
        self.write(f"Game over. Score: {self.score}    High score: {self.highscore}",align="center",font=('Arial',30,'normal'))

    def reset(self):
        if self.score > int(self.highscore):
            self.highscore = self.score

            with open('Classic Snake Game/data.txt','w') as f:
                new_highscore = str(self.highscore)
                f.write(new_highscore)
                f.close()

        self.score = 0
        self.hideturtle()
        self.penup()
        self.color('white')
        self.goto(0,240)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}    High score: {self.highscore}",align="center",font=('Arial',14,'normal'))

