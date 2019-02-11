from turtle import *

mos = Turtle()
screen = Screen()

mos.color("turquoise")
mos.pensize(5)
mos.speed(6)
mos.turtlesize(1,1,1)
mos.shape("turtle")
screen.bgcolor("black")


def drawHex():
	for x in range(6):
		mos.forward(75)
		mos.left(60)
drawHex()

mainloop()