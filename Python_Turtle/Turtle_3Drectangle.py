# Shape Mid left (rectangle)

# import package
import turtle

# define details
turtle.speed(0)

turtle.showturtle()
turtle.pendown()
turtle.goto(300,0)
turtle.goto(300,-300)
turtle.goto(0,0)

turtle.goto(-300,300)
turtle.goto(-300,0)
turtle.goto(0,0)

turtle.goto(0,300)
turtle.goto(-300,300)
turtle.home()

turtle.goto(0,-300)
turtle.goto(300,-300)

turtle.goto(300,0)
turtle.goto(0,300)

turtle.goto(0,-300)
turtle.goto(-300,0)
turtle.hideturtle()

# close program
turtle.done()