from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.position = position
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=7, stretch_len=1)
        self.goto(self.position, 0)
        
    def up(self):
        new_y = self.ycor() + 60
        if self.ycor() < 220:
            self.goto(self.xcor(), new_y)
    
    def down(self):
        new_y = self.ycor() - 60
        if self.ycor() > -220:
            self.goto(self.xcor(), new_y)
