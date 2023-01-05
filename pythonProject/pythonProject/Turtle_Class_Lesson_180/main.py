import time
from turtle import Turtle, Screen
from snake import Snake

screen = Screen()
screen.screensize(600, 600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake() # It triggers start_position() in def __init__(self) in Snake class

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Down")
screen.onkey(snake.right, "Down")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(1)
    snake.move()


screen.exitonclick()

