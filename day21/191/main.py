from turtle import Screen
from snake import Snake
from food import Food
import time

game_is_on = True

# Create an instance of the Screen Object and set width and height
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
# Stop Refreshing the Screen (force refresh with screen.update())
screen.tracer(0)

# Create Snake and Food Object
snake = Snake()
food = Food()

# Listen for the pressed keys
screen.listen()
screen.onkey(snake.move_right, "Right")
screen.onkey(snake.move_left, "Left")
screen.onkey(snake.move_up, "Up")
screen.onkey(snake.move_down, "Down")

while game_is_on:
    # We only update the screen only when all pieces moved
    screen.update()
    time.sleep(0.1)
    snake.move()

    #Detect collusion with food


# The screen does not just disappear
screen.exitonclick()
