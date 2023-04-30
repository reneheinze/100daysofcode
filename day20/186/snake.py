from turtle import Screen, Turtle


class Snake:
    my_segments = []

    def __init__(self):
        self.create_segments(3)
        self.set_segment_start()

    def create_segments(self, segment_number):
        """Get a integer number as input and create and return a segment object list"""
        for _ in range(segment_number):
            segment = Turtle(shape="square")
            segment.color("white")
            self.my_segments.append(segment)

    def set_segment_start(self):
        """Gets the turtles list and puts them on the start position"""
        start_position = 0
        for segment in self.my_segments:
            segment.penup()
            segment.goto(x=start_position, y=0)
            start_position -= 20

    def move_right(self):
        """Turns the arrow 90 degrees to the right"""
        self.my_segments[0].right(90)

    def move_left(self):
        """Turns the arrow 90 degrees to the left"""
        self.my_segments[0].left(90)

    def move(self):
        """Starts moving the snake. Use d and a to navigate"""
        screen = Screen()
        screen.listen()
        for seg_num in range(len(self.my_segments) - 1, 0, -1):
            # get x and y of the connected segment
            new_x = self.my_segments[seg_num - 1].xcor()
            new_y = self.my_segments[seg_num - 1].ycor()
            # set the new position of the current segment to where the connected segment was
            self.my_segments[seg_num].goto(new_x, new_y)
        # Move Head segment forward
        self.my_segments[0].forward(20)
        screen.onkey(self.move_right, "d")
        screen.onkey(self.move_left, "a")