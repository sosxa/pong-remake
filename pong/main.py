from turtle import Turtle
from turtle import Screen
from sliders import Sliders
from ball import Ball
from scoreboard import Scoreboard
import time


# screen settings
screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)


r_slider = Sliders((350, 0))
l_slider = Sliders((-350, 0))
ball = Ball()
scoreboard = Scoreboard()


screen.listen()
screen.onkeypress(r_slider.up, "Up")
screen.onkeypress(r_slider.down, "Down")
screen.onkeypress(l_slider.up, "w")
screen.onkeypress(l_slider.down, "s")
	
		
game_on = True
while game_on:
	time.sleep(ball.move_speed)
	screen.update()
	ball.move()
	# contact with wall
	if ball.ycor() > 280 or ball.ycor() < -280:
		ball.bounce_y()
	# the ball automatically goes to 10 10 in the start and once it hits the wall it does the ycor 10 * -1 and than that makes it go down you dont change the x since the ball is already moiving	
	# contact with right slider
	if ball.distance(r_slider) < 50 and ball.xcor() > 320 or ball.distance(l_slider) < 50 and ball.xcor() > -320:
		ball.bounce_x()
	# ball barrier
	if ball.xcor() > 380:
		ball.reset_position()
		scoreboard.left_score()
	if ball.xcor() < -380:
		ball.reset_position()
		scoreboard.right_score()
		
screen.exitonclick()
