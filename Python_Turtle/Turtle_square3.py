# Turtle Graphics: Repeating Squares

# import package
import turtle

# define details
turtle.showturtle()
turtle.setheading(180)
turtle.penup()
turtle.goto(200,-200)
turtle.hideturtle()
turtle.pendown()
turtle.speed(0)

# define variable and for loop
move = 4

for x in range (100):
    move += 4
    for y in range (4):
        turtle.forward(move)
        turtle.right(90)

# close program
turtle.done()