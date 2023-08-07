from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")

class Scorebook(Turtle):
    def __init__(self):
        super().__init__()
        self.scoretext = ""
        self.score = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 275)
        self.displayscore()


    def displayscore(self):
        self.clear()
        self.scoretext = f"Score: {self.score}"
        self.write(self.scoretext, move=False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
