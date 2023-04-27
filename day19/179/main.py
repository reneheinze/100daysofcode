from turtle import Turtle, Screen
import random


def create_turtle_objects(color_list):
    """Get a string color list as input and create and return a turtle object list"""
    turtles = []
    for color in color_list:
        turtle = Turtle(shape="turtle")
        turtle.color(color)
        turtles.append(turtle)
    return turtles


def set_start_position(turtle_objects):
    """Get a turtle object list and set them in position"""
    # get the total number of turtle objects
    total_turtles = len(turtle_object)
    # get the start distance between the turtles
    start_distance = (screen_height / 2) / total_turtles
    # get the start position
    start_position = (start_distance * total_turtles) / 2
    # iterate through the turtle objects and bring them in position
    for turtle in turtle_objects:
        turtle.penup()
        turtle.goto(x=-450, y=start_position)
        start_position -= start_distance


screen = Screen()
screen_width = 1000
screen_height = 1000
is_race_on: False

# Screen setup with a windows of 1000x1000 Pixel
# Using positional arguments to better understand whats going on later
screen.setup(width=screen_width, height=screen_height)

# Messagebox to ask for the winner
user_bet = screen.textinput(title="Make you bet", prompt="Which turtle will win the race? Enter a color: ")
color_list = ["red", "orange", "yellow", "green", "blue", "purple"]

# Create turtle objects
turtle_object = create_turtle_objects(color_list)
# Set turtles to starting position
set_start_position(turtle_object)

# Check if user_bet is set
if user_bet:
    is_race_on = True

# Start the race
while is_race_on:
    for turtle in turtle_object:
        turtle.forward(random.randint(1,10))

        # Check if the goal line is reached
        if turtle.xcor() > 500:
            is_race_on = False
            if turtle.fillcolor() == user_bet.lower():
                print(f"You win. The {turtle.fillcolor()} Turtle is the winner.")
            else:
                print(f"You loose. The {turtle.fillcolor()} Turtle is the winner.")


# Start Listening for Events
screen.listen()
# screen.onkey(move_forwards,"w")

screen.exitonclick()

