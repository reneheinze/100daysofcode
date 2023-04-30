from turtle import Screen, Turtle
import time


def create_segments(segment_number):
    """Get a integer number as input and create and return a segment object list"""
    segments = []
    for _ in range(segment_number):
        segment = Turtle(shape="square")
        segment.color("white")
        segments.append(segment)
    return segments


def set_segment_start(segments):
    """Gets the turtles list and puts them on the start position"""
    start_position = 0
    for segment in segments:
        segment.penup()
        segment.goto(x=start_position, y=0)
        start_position -= 20

def move_right():
    """Turns the arrow 90 degrees to the right"""
    my_segments[0].right(90)

def move_left():
    """Turns the arrow 90 degrees to the left"""
    my_segments[0].left(90)

# segments list
my_segments = []

game_is_on = True

# Create an instance of the Screen Object and set width and height
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
# Stop Refreshing the Screen (force refresh with screen.update())
screen.tracer(0)

# Create My Turtles
my_segments = create_segments(3)

# Set Turtles Start Position
set_segment_start(my_segments)

while game_is_on:
    # We only update the screen only when all pieces moved
    screen.update()
    time.sleep(0.1)
    screen.listen()
    # Get the current position of all segments and put it into a list
    position = [my_segments[0].position(),my_segments[1].position()]
    # Move Head segment forward
    my_segments[0].forward(20)
    # ! Only 2 and 1 will be used for iteration.
    for items in range(2, 0, -1):
        segment_position = position[items-1]
        my_segments[items].goto(segment_position)
    screen.onkey(move_right, "d")
    screen.onkey(move_left, "a")

# The screen does not just disappear
screen.exitonclick()
