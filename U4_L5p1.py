from turtle import *

mos = Turtle()
screen = Screen()

mos.color("turquoise")
mos.pensize(5)
mos.speed(6)
mos.turtlesize(1,1,1)
mos.shape("turtle")
screen.bgcolor("black")


def drawTriangle():
	for x in range(3):
		mos.forward(75)
		mos.left(120)

for x in range(12):
	drawTriangle()
	mos.left(30)







mainloop()