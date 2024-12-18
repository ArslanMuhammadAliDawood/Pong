from turtle import Screen
from Paddle import Paddle
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)


player1 = Paddle(x_position=350, y_position=0)
player2 = Paddle(x_position=-350, y_position=0)


screen.listen()
screen.onkey(player1.move_up, "Up")
screen.onkey(player1.move_down, "Down")
screen.onkey(player2.move_up, "w")
screen.onkey(player2.move_down, "s")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
















screen.exitonclick()
