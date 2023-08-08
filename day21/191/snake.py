from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

start_pos = []

class Snake:


    def __init__(self):
        self.my_segments = []
        self.create_start_position(3)
        self.create_snake()
#        self.head = self.my_segments[0]

    def create_snake(self):
        for position in start_pos:
            self.add_segment(position)


    def add_segment(self, position):
        """Get a integer number as input and create and return a segment object list"""
        segment = Turtle(shape="square")
        segment.color("white")
        segment.penup()
        segment.goto(position)
        self.my_segments.append(segment)

    def extend(self):
        self.add_segment(self.my_segments[-1].position())

    def create_start_position(self, start_range):
        """Gets the turtles list and puts them on the start position"""
        x = 0
        for position in range(start_range):
            start_pos.append((x, 0))
            x -= 20
        print(start_pos)

    def move_right(self):
        """Turns the arrow to the right"""
        if self.my_segments[0].heading() != LEFT:
            self.my_segments[0].setheading(RIGHT)

    def move_left(self):
        """Turns the arrow to the left"""
        if self.my_segments[0].heading() != RIGHT:
            self.my_segments[0].setheading(LEFT)

    def move_up(self):
        """Turns the arrow up"""
        if self.my_segments[0].heading() != DOWN:
            self.my_segments[0].setheading(UP)

    def move_down(self):
        """Turns the arrow down"""
        if self.my_segments[0].heading() != UP:
            self.my_segments[0].setheading(DOWN)

    def move(self):
        """Starts moving the snake."""
        for seg_num in range(len(self.my_segments) - 1, 0, -1):
            # get x and y of the connected segment
            new_x = self.my_segments[seg_num - 1].xcor()
            new_y = self.my_segments[seg_num - 1].ycor()
            # set the new position of the current segment to where the connected segment was
            self.my_segments[seg_num].goto(new_x, new_y)
        # Move Head segment forward
        self.my_segments[0].forward(MOVE_DISTANCE)
