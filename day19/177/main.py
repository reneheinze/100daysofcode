from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forwards():
    tim.forward(10)


# Start Listening for Events
screen.listen()
screen.onkey(move_forwards,"space")
screen.exitonclick()
