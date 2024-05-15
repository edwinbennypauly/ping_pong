from turtle import Screen,Turtle
import time

from ball import Ball
from paddles import Paddles
from scoreboard import  ScorBoard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)
center_line = Turtle()
center_line.color("white")
center_line.penup()
center_line.goto(0,300)
for i in range(30):
    if i % 2 ==0:
        center_line.penup()
        center_line.forward(10)
    else:
        center_line.pendown()
        center_line.forward(10)

center_line.hideturtle()

ball = Ball()
scoreboard = ScorBoard()



l_paddle = Paddles((-350,0))
r_paddle = Paddles((350,0))

screen.listen()

screen.onkey(fun=r_paddle.go_up,key="Up")
screen.onkey(fun=r_paddle.go_down,key="Down")
screen.onkey(fun=l_paddle.go_up,key="w")
screen.onkey(fun=l_paddle.go_down,key="s")

game_is_on = True

while game_is_on:

    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    # collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()
    # collision with paddle
    if ball.distance(l_paddle)<50 and ball.xcor() < - 340:
        ball.hit()
        scoreboard.l_score += 1
        scoreboard.refresh()

    if ball.distance(r_paddle) <50 and ball.xcor() > 340 :
        ball.hit()
        scoreboard.r_score +=1
        scoreboard.refresh()




    if ball.xcor() > 380:
        scoreboard.r_score -= 1
        scoreboard.refresh()
        ball.reset_postion()
    if ball.xcor() < -380:
        scoreboard.l_score -= 1
        scoreboard.refresh()
        ball.reset_postion()


















screen.exitonclick()
