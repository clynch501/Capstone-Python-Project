# Turtle Shapes as Functions
import turtle

# Square Function, starting coordinates x and y start at the bottom left corner,
def square(x, y, width, color):
    turtle.penup() 
    turtle.goto(x, y) 
    turtle.fillcolor(color) 
    turtle.pendown() 
    turtle.begin_fill()
    for count in range(4):
        turtle.forward(width)
        turtle.left(90)
    turtle.end_fill()
    
# Circle Function, the x and y are the center of the circle
def circle(x, y, radius, color):
    turtle.penup()
    turtle.goto(x, y)
    turtle.fillcolor(color)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()
    
# Line Function
def line(startX, startY, endX, endY, color):
    turtle.penup() 
    turtle.goto(startX, startY)
    turtle.pendown()
    turtle.pencolor(color)
    turtle.goto(endX, endY)

# Pentagon Function
def pentagon(x,y,length,color):
    turtle.penup()
    turtle.goto(x,y)
    turtle.fillcolor(color)
    turtle.pendown()
    turtle.begin_fill()
    for side in range(5):
        turtle.forward(length) #Length of each side
        turtle.right(72) #Angle
    turtle.end_fill()
        

