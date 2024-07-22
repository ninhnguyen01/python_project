# Shape Bottom Right (square)

# import package
import turtle

# define details
turtle.speed(0)

turtle.showturtle()
turtle.dot()
turtle.goto(100,100)
turtle.dot()
turtle.goto(100,-100)
turtle.dot()
turtle.home()
turtle.goto(-100,100)
turtle.dot()
turtle.goto(-100,-100)
turtle.dot()
turtle.home()

turtle.penup()
turtle.goto(-100,100)

turtle.pendown()
turtle.forward(25)

turtle.penup()
turtle.forward(25)

turtle.pendown()
turtle.forward(35)

turtle.penup()
turtle.forward(25)

turtle.pendown()
turtle.forward(35)

turtle.penup()
turtle.forward(25)

turtle.pendown()
turtle.forward(30)

turtle.penup()
turtle.goto(-100,-100)

turtle.pendown()
turtle.forward(25)

turtle.penup()
turtle.forward(25)

turtle.pendown()
turtle.forward(35)

turtle.penup()
turtle.forward(25)

turtle.pendown()
turtle.forward(35)

turtle.penup()
turtle.forward(25)

turtle.pendown()
turtle.forward(30)
turtle.hideturtle()

# close program
turtle.done()