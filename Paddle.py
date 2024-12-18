from turtle import Turtle

class Paddle:
    def __init__(self):
        self.turtle = Turtle(shape="square")
        self.create_paddle()


    def create_paddle(self):
        self.turtle.color("white")
        self.turtle.shapesize(stretch_wid=5,
                              stretch_len=1)  # stretch_wid, and stretch_len refer to the height and width of the object, respectively.
        self.turtle.penup()
        self.turtle.goto(350,0)

    def move_up(self):
        """ Move Paddle Up"""
        y_position = self.turtle.ycor() + 20
        self.turtle.goto(self.turtle.xcor(), y_position)

    def move_down(self):
        """ Move paddle down """
        y_position = self.turtle.ycor() + -20
        self.turtle.goto(self.turtle.xcor(), y_position)

























