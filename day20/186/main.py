from turtle import Screen, Turtle
from snake import Snake
import time

game_is_on = True

# Create an instance of the Screen Object and set width and height
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
# Stop Refreshing the Screen (force refresh with screen.update())
screen.tracer(0)

# Create Snake Object
snake = Snake()

while game_is_on:
    # We only update the screen only when all pieces moved
    screen.update()
    time.sleep(0.1)
    snake.move()



# The screen does not just disappear
screen.exitonclick()
