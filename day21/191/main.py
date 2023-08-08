from turtle import Screen
from snake import Snake
from food import Food
from scorebook import Scorebook
import time

game_is_on = True

# Create an instance of the Screen Object and set width and height
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
# Stop Refreshing the Screen (force refresh with screen.update())
screen.tracer(0)

# Create Snake and Food Object and Score Book
snake = Snake()
food = Food()
scorebook = Scorebook()

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

    #Detect collision with food
    if snake.my_segments[0].distance(food) < 15:
        scorebook.score += 1
        scorebook.displayscore()
        snake.extend()
        food.refresh()

    #Detect collision with head
    # Slice the list of segments from my snake. Get everything inside the list other than the first item.
    for segment in snake.my_segments[1:]:
        if snake.my_segments[0].distance(segment) < 10:
            scorebook.game_over()
            game_is_on = False

    #Detect collision with wall
    if snake.my_segments[0].xcor() > 280 or snake.my_segments[0].xcor() < -280 or snake.my_segments[0].ycor() < -280 or snake.my_segments[0].ycor() > 280:
        scorebook.game_over()
        game_is_on = False

# The screen does not just disappear
screen.exitonclick()
