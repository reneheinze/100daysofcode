# Import the Class
from turtle import Screen
import random, colorgram
import turtle as turtle_module

def create_rgb_tuple(color_list_rgb):
    """Takes the RGB attribute from the color object and iterates through it.
    Returns a tuple with only the RGB data"""
    rgb_list = []
    # Iterate through the RGB attribute
    for rgb in color_list_rgb:
        rgb_list.append(rgb)
    # Convert the list to a tuple
    rgb_tuple = tuple(rgb_list)
    return rgb_tuple


def create_rgb_list(color_list):
    # Create a empty list for the color tuples
    color_tuple_list = []
    for color in color_list:
        color_tuple_list.append(create_rgb_tuple(color.rgb))
    return color_tuple_list


# Extract Colors from Image
color_list = colorgram.extract("Painting.png", 30)

# Create and Print Tuple List
tuple_color_list = create_rgb_list(color_list)
# print(tuple_color_list)

# It is going to created from the turtle module. And inside that module there is a turtle class.
tim = turtle_module.Turtle()
tim.hideturtle()
tim.color("black")
# Create Screen Object
screen = Screen()
# Set Colormode for RGB function
screen.colormode(255)

tim.degrees(90)
tim.penup()
position_y = -200
number_of_dots = 101
tim.speed(10)
tim.setposition(-220, position_y)
tim.speed(3)

# Set position
for dot_count in range (1, number_of_dots):
    tim.color(random.choice(tuple_color_list))
    tim.dot(20)
    tim.forward(50)

# Draw line
    if dot_count % 10 == 0:
        position_y += 50
        tim.speed(10)
        tim.setposition(-220, position_y)
        tim.speed(3)




screen.exitonclick()
