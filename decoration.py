from turtle import Turtle


class SmartBoard:
    def __init__(self):
        self.l_board = Turtle()
        self.l_board.hideturtle()
        self.r_board = Turtle()
        self.r_board.hideturtle()
        self.combo = Turtle()
        self.combo.hideturtle()
        self.border = Turtle()
        self.border.hideturtle()
        self.combo_score = 0
        self.bobder()

    def l_part(self):
        l = self.l_board
        l.penup()
        l.goto(-400,-300)
        l.pendown()
        l.fillcolor("gray")
        l.begin_fill()
        l.fd(400)
        l.lt(90)
        l.fd(600)
        l.lt(90)
        l.fd(400)
        l.lt(90)
        l.fd(600)
        l.end_fill()

    def r_part(self):
        r = self.r_board
        r.penup()
        r.goto(0, -300)
        r.pendown()
        r.fillcolor("gray")
        r.begin_fill()
        r.fd(400)
        r.lt(90)
        r.fd(600)
        r.lt(90)
        r.fd(400)
        r.lt(90)
        r.fd(600)
        r.end_fill()

    def clear(self):
        self.l_board.clear()
        self.r_board.clear()

    def update(self):
        self.combo.penup()
        self.combo.goto(0, 250)
        self.combo.pencolor("green")
        self.combo.clear()
        self.combo.write(f"{self.combo_score}", align="center", font=("arial", 20, "bold"))

    def combo_strick(self):
        self.combo_score += 1
        self.update()

    def resetc(self):
        self.combo_score = 0
        self.update()

    def bobder(self):
        bo = self.border
        bo.pensize(3)
        bo.pencolor("gray")
        bo.penup()
        bo.goto(0, -300)
        bo.lt(90)
        for _ in range(35):
            bo.pendown()
            bo.fd(10)
            bo.up()
            bo.fd(5)

