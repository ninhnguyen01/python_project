# Turtle Graphics: Triangle Function

# import package
import turtle

# define details
turtle.showturtle()
turtle.speed(0)
turtle.penup()

# triangle function
def triangle():
    coord_1()
    coord_2()
    coord_3()

# coordinates function
def coord_1():
    turtle.goto(-100,0)
    turtle.pendown()
    turtle.pencolor('red')
    turtle.goto(0,100)
   
def coord_2():
    turtle.pencolor('green')
    turtle.goto(100,0)
    
def coord_3():
    turtle.pencolor('blue')
    turtle.goto(-100,0)
    turtle.hideturtle()

triangle()

# close program
turtle.done()