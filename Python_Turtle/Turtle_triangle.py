# Shape Top Right (triangle)

# import package
import turtle

# define details
turtle.speed(0)

turtle.showturtle()
turtle.penup()
turtle.goto(0,200)
turtle.pendown()
turtle.goto(150,-150)
turtle.home()
turtle.goto(-150,-150)
turtle.goto(0,200)
turtle.penup()

turtle.goto(150,-150)
turtle.pendown()
turtle.goto(-150,-150)
turtle.hideturtle()

# close program
turtle.done()