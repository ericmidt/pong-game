from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, starting_position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.penup()
        self.setheading(90)
        self.goto(starting_position)

    def move_up(self):
        self.setheading(90)
        self.forward(50)

    def move_down(self):
        self.setheading(270)
        self.forward(50)
