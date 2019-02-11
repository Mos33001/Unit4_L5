from turtle import *

mos = Turtle()
screen = Screen()

mos.color("turquoise")
mos.pensize(5)
mos.speed(6)
mos.turtlesize(1,1,1)
mos.shape("turtle")
screen.bgcolor("black")


def drawHex(side):
	for x in range(6):
		mos.forward(side)
		mos.left(60)
drawHex(30)
drawHex(50)
drawHex(70)
drawHex(90)
drawHex(110)
drawHex(130)
drawHex(150)
drawHex(170)
drawHex(190)


mainloop()