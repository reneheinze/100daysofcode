from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forwards():
    tim.forward(100)

def move_backwards():
    tim.backward(100)

def move_right():
    tim.right(10)

def move_left():
    tim.left(10)

def clear_screen():
    tim.reset()

# Start Listening for Events
screen.listen()
screen.onkey(move_forwards,"w")
screen.onkey(move_backwards,"s")
screen.onkey(move_right,"d")
screen.onkey(move_left,"a")
screen.onkey(clear_screen,"c")
screen.exitonclick()
