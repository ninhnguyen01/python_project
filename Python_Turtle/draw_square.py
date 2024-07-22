# Turtle Graphics: Modularizing Code with Functions

# import package
import turtle

# draw square
turtle.fillcolor('blue')
turtle.begin_fill()

for count in range (4):
    turtle.forward(100)
    turtle.left(90)
turtle.end_fill()

# close program
turtle.done()
