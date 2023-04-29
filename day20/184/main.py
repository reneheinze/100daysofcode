from turtle import Screen, Turtle


def create_turtle_objects(turtle_number):
    """Get a integer number as input and create and return a turtle object list"""
    turtles = []
    for _ in range(turtle_number):
        turtle = Turtle(shape="square")
        turtle.color("white")
        turtles.append(turtle)
        # Max Speed to speed up goto method
        turtle.speed(0)
    return turtles


def set_turtle_start(turtles):
    """Gets the turtles list and puts them on the start position"""
    start_position = 0
    for turtle in turtles:
        turtle.penup()
        turtle.goto(x=start_position, y=0)
        start_position -= 20


# Create an instance of the Screen Object and set width and height
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")

# Create My Turtles
my_turtles = create_turtle_objects(3)

# Set Turtles Start Position
set_turtle_start(my_turtles)

# The screen does not just disappear
screen.exitonclick()
