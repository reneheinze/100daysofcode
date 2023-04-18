from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forwards():
    """Moves the arrow 100 steps forward"""
    tim.forward(100)

def move_backwards():
    """Moves the arrow 100 steps backwards"""
    tim.backward(100)

def move_right():
    """Turns the arrow 10 degrees to the right"""
    tim.right(10)

def move_left():
    """Turns the arrow 10 degrees to the left"""
    tim.left(10)

def clear_screen():
    """Clears the screen and resets the arrow to its initial position"""
    tim.reset()

# Start Listening for Events
screen.listen()
screen.onkey(move_forwards,"w")
screen.onkey(move_backwards,"s")
screen.onkey(move_right,"d")
screen.onkey(move_left,"a")
screen.onkey(clear_screen,"c")
screen.exitonclick()
