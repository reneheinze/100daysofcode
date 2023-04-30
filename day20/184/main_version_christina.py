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
    for seg_num in range(len(my_segments)-1, 0, -1):
        # get x and y of the connected segment
        new_x = my_segments[seg_num - 1].xcor()
        new_y = my_segments[seg_num - 1].ycor()
        # set the new position of the current segment to where the connected segment was
        my_segments[seg_num].goto(new_x,new_y)
    # Move Head segment forward
    my_segments[0].forward(20)
    screen.onkey(move_right, "d")
    screen.onkey(move_left, "a")

# The screen does not just disappear
screen.exitonclick()
