# Turtle Graphics: STOP Sign

# import package
import turtle

# define details
turtle.showturtle()
turtle.penup()
turtle.goto(-50,100)
turtle.pendown()
turtle.speed(8)

# for loop
for x in range (8):
    turtle.forward(100)
    turtle.right(45)

turtle.penup()
turtle.goto(-15,-30)
turtle.pendown()
turtle.write('STOP',font=20)
turtle.hideturtle()

# close program
turtle.done()