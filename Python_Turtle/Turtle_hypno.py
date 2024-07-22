# Turtle Graphics Hypnotic Pattern

# import package
import turtle

# define details
turtle.showturtle()
turtle.pendown()
turtle.setheading(90)
turtle.speed(10)

# define move variable and for loop
move = 5

for x in range (12):
    for y in range (4):
        turtle.forward(move)
        turtle.left(90)
        turtle.hideturtle()
        move += 5

# close program
turtle.done()