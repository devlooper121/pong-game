from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.l_sc = 0
        self.r_sc = 0

        self.update()

    def update(self):
        self.clear()
        self.goto(-200, 250)
        self.write(f"{self.l_sc}", align="center", font=("arial", 20, "bold"))
        self.goto(200, 250)
        self.write(f"{self.r_sc}", align="center", font=("arial", 20, "bold"))

    def l_score(self):
        self.l_sc += 1
        self.update()

    def r_score(self):
        self.r_sc += 1
        self.update()
