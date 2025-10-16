# Combining shape functions
# Square, circle, line and pentagon

import turtle
import my_graphics as shape

def main():
    shape.square(-100,100,50,'blue')
    shape.square(-100,-100,50,'blue')
    shape.pentagon(0,0,50,'red')
    shape.circle(0,0,50, 'green')
    shape.line(-100,-100,100,-100,'black')

main()

