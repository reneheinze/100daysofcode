# Import the Class
from turtle import Turtle, Screen
import random


def draw_square():
    """draws a square with the turtle"""
    for _ in range(4):
        tim.forward(250)
        tim.left(90)


def draw_deshline():
    """draws a single straight deshline"""
    for number in range(1, 50):
        if number % 2 == 0:
            tim.down()
            tim.forward(5)
        else:
            tim.up()
            tim.forward(5)


def draw_object(sites, angle):
    """Draws an object. It takes the number of sites and the angle as parameters.
    It is only called from the draw_different_shapes function"""
    tim.pencolor(random_color())
    for _ in range(sites):
        tim.right(angle)
        tim.forward(100)


def draw_diffent_shapes(object_sites):
    """Draws different shapes. Depend on the number of object_sites you give as a parameter.
    For the drawing it uses draw_object"""
    while object_sites < 12:
        # Calculate each angle
        angle = 360 / object_sites
        draw_object(object_sites, angle)
        object_sites += 1


def draw_randomwalk(steps):
    """draws a random walk. It takes the number if steps in the walk as a parameter."""
    # define command lists
    list = ["tim.right(90)", "tim.left(90)", "tim.forward(25)", "tim.back(25)"]
    tim.speed(0)
    tim.pensize(10)

    for _ in range(2000):
        eval(random.choice(list))
        tim.pencolor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        tim.pencolor(random_color())


def random_color():
    """generates an RGB tuple and returns it"""
    my_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    return my_color


def draw_spirograph(circle_counts):
    angle = 360 / circle_counts
    tim.setheading(0)
    tim.speed(0)

    for _ in range(circle_counts):
        tim.pencolor(random_color())
        tim.circle(80)
        tim.left(angle)

# Create a Turtle Class
tim = Turtle()
tim.shape("turtle")
tim.color("blue1")
# Create Screen Object
screen = Screen()
# Set Colormode for RGB function
screen.colormode(255)

print(type(tim))
print(tim)


# Draw Square
# draw_square


# Draw DeshLine
# draw_deshline()

# Draw different shapes
# draw_diffent_shapes(3)

# Draw Randomwork
#draw_randomwalk(500)

# Draw Spirograph
#draw_spirograph(100)




screen.exitonclick()
