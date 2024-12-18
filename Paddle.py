from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, x_position, y_position):
        super().__init__()
        self.shape("square")
        self.x_position = x_position
        self.y_position = y_position
        self.create_paddle()

    def create_paddle(self):
        self.color("white")
        self.shapesize(stretch_wid=5,
                              stretch_len=1)  # stretch_wid, and stretch_len refer to the height and width of the object, respectively.
        self.penup()
        self.goto(self.x_position,self.y_position)

    def move_up(self):
        """ Move Paddle Up"""
        y_position = self.ycor() + 20
        self.goto(self.xcor(), y_position)

    def move_down(self):
        """ Move paddle down """
        y_position = self.ycor() + -20
        self.goto(self.xcor(), y_position)

























