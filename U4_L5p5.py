from turtle import *

mos = Turtle()
screen = Screen()

mos.color("turquoise")
mos.pensize(5)
mos.speed(6)
mos.turtlesize(1,1,1)
mos.shape("turtle")
screen.bgcolor("black")

def row():
	def drawStar():
		for x in range(5):
			mos.forward(75)
			mos.left(144)

	mos.penup()
	mos.goto(-200,0)
	mos.pendown()		
	drawStar()
		
	
	mos.penup()
	mos.goto(0,0)
	mos.pendown()		
	drawStar()
	
	mos.penup()
	mos.goto(200,0)
	mos.pendown()		
	drawStar()




row()

mainloop()