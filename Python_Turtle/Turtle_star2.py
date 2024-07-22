# Turtle Graphics: Star Pattern

# import package
import turtle 

# define details
turtle.showturtle()
turtle.penup()
turtle.goto(-150,-50)
turtle.pendown()
turtle.speed(5)

# for loop
for x in range (8):
    turtle.forward(300)
    turtle.left(135)
    turtle.hideturtle()

# close program
turtle.done()