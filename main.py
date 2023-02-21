from turtle import Screen
import time
from food import Food
from snake import Snake
from scoreboard import ScoreBoard

my_screen = Screen()
my_screen.setup(width=600, height=600)
my_screen.bgcolor("black")
my_screen.title("Snake Game")
my_screen.tracer(0)

my_snake = Snake()
my_food = Food()
my_score = ScoreBoard()

my_screen.listen()
my_screen.onkeypress(my_snake.up, "Up")
my_screen.onkeypress(my_snake.down, "Down")
my_screen.onkeypress(my_snake.left, "Left")
my_screen.onkeypress(my_snake.right, "Right")

my_snake.create_snake()
game_in_on = True

while game_in_on:
    my_screen.update()
    time.sleep(.1)
    my_snake.snake_move()

    # to detect collision

    if my_snake.head.distance(my_food) < 20:
        my_food.refresh()
        my_snake.extend()
        my_score.clear()
        my_score.increase_score()
    # detects if game over

    if my_snake.head.xcor() > 290 or my_snake.head.xcor() < -290 or my_snake.head.ycor() > 290 or my_snake.head.ycor() \
            < -290:
        my_score.reset()
        my_snake.reset()

    # detect if head collides with any of its part(using concept of slicing a part of list)
    for segments in my_snake.segments[1:]:

        if my_snake.head.distance(segments) < 15:
            my_score.reset()
            my_snake.reset()

my_screen.exitonclick()
