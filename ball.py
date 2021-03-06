from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.pause = 0
        self.x_move = 10
        self.y_move = 10

    def move(self):
        if self.pause == 0:
            new_x = self.xcor() + self.x_move
            new_y = self.ycor() + self.y_move
            self.goto(new_x, new_y)

    def y_bounce(self):
        self.y_move *= -1

    def side_bounce(self):
        self.x_move *= -1

    def ball_service(self):
        self.goto(0, 0)
        self.x_move *= -1
        # self.y_move *= -1

    def play_pause(self):
        if self.pause == 0:
            self.pause = 1
        else:
            self.pause = 0
