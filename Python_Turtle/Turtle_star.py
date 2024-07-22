# Turtle Graphics: Star Pattern

# import package
import turtle

# define details
turtle.showturtle()
turtle.penup()
turtle.goto(250,-100)
turtle.pendown()
turtle.speed(5)

# for loop
for x in range (8):
        turtle.goto(-250,-100)
        turtle.goto(100,250)
        turtle.goto(100,-250)
        turtle.goto(-250,100)
        turtle.goto(250,100)
        turtle.goto(-100,-250)
        turtle.goto(-100,250)
        turtle.goto(250,-100)
        turtle.penup()
        turtle.hideturtle()

# close program
turtle.done()