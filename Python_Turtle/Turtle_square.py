# Turtle Graphics Drawing

# Shape Top Left (2 square)

# import package
import turtle

# define details
turtle.speed(0)

turtle.showturtle()
turtle.heading()
turtle.penup()
turtle.goto(300,0)

turtle.heading()
turtle.pendown()
turtle.goto(150,150)
turtle.goto(0,0)

turtle.pos()
turtle.heading()
turtle.goto(-150,-150)
turtle.goto(-300,0)
turtle.goto(-150,150)

turtle.goto(0,0)
turtle.goto(150,-150)
turtle.goto(300,0)
turtle.hideturtle()

# close program
turtle.done()