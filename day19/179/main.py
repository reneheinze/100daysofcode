from turtle import Turtle, Screen

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
    #get the total number of turtle objects
    total_turtles = len(turtle_object)
    #get the start distance between the turtles
    start_distance = (screen_height / 2) / total_turtles
    #get the start position
    start_position = (start_distance*total_turtles)/2
    #iterate through the turtle objects and bring them in position
    for turtle in turtle_objects:
        turtle.penup()
        turtle.goto(x=-450,y=start_position)
        start_position -= start_distance


screen = Screen()
screen_width=1000
screen_height=1000

# Screen setup with a windows of 1000x1000 Pixel
# Using positional arguments to better understand whats going on later
screen.setup(width=screen_width,height=screen_height)

# Messagebox to ask for the winner
#user_bet = screen.textinput(title="Make you bet", prompt="Which turtle will win the race? Enter a color: ")
color_list = ["red", "orange", "yellow", "green", "blue", "purple"]

# Create turtle objects
turtle_object = create_turtle_objects(color_list)
print(turtle_object[0].position())
set_start_position(turtle_object)

print(turtle_object[0].position())


# Start Listening for Events
screen.listen()
#screen.onkey(move_forwards,"w")

screen.exitonclick()

#test
