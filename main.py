from snake import Snake, screen
from food import Food
from scoreboard import Scoreboard
import turtle

snake = Snake()
snake.create()

food = Food()
food.reposition()

screen.listen()
screen.onkeypress(snake.dir_right,"Right")
screen.onkeypress(snake.dir_left,"Left")
screen.onkeypress(snake.dir_forward,"Up")
screen.onkeypress(snake.dir_back,"Down")

def die():
    turtle.bye()

screen.onkeypress(die,"q")

score = Scoreboard()
 
while True:
    snake.move()
    if snake.segments[0].distance(food) < 16:
        food.reposition()
        score.increase_score()
        snake.extend()
    if snake.segments[0].xcor() == -300 or snake.segments[0].ycor() == -300 or snake.segments[0].xcor() == 300 or snake.segments[0].ycor() == 300:
        score.reset()
        snake.reset()

    for segment in snake.segments:
        if snake.segments[0].distance(segment) < 10:
            if segment == snake.segments[0]:
                pass
            else:
                score.reset()
                snake.reset()
        
    
    

