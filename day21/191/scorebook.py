from turtle import Turtle


class Scorebook(Turtle):
    def __init__(self):
        super().__init__()
        self.scoretext = ""
        self.score = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 280)
        self.displayscore()


    def displayscore(self):
        self.clear()
        self.scoretext = f"Score: {self.score}"
        self.write(self.scoretext, move=False, align="center", font=("Arial", 16, "normal"))
