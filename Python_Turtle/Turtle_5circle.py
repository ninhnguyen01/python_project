# Shape Mid Right (five circle)

# import package
import turtle

# define details
turtle.speed(0)

turtle.showturtle()
turtle.penup()
turtle.goto(0,-50)
turtle.pendown()
turtle.circle(50)

turtle.penup()
turtle.goto(65,-100)
turtle.pendown()
turtle.circle(50)

turtle.penup()
turtle.goto(130,-50)
turtle.pendown()
turtle.circle(50)

turtle.penup()
turtle.goto(-65,-100)
turtle.pendown()
turtle.circle(50)

turtle.penup()
turtle.goto(-130,-50)
turtle.pendown()
turtle.circle(50)
turtle.hideturtle()

# close program
turtle.done()