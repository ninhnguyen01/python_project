# Turtle Graphics: Modular Snowman

# import package
import turtle

# define details
turtle.showturtle()
turtle.penup()
turtle.speed(0)

# main function
def main():
    drawBase(0,-75,75)
    drawMidsection(0,50,50)
    drawArms(-50,50)
    drawHead(0,130,30)
    drawHat(0,150)

# draw function
def drawBase(x,y,radius):
    turtle.goto(x,y - radius)
    turtle.pendown()
    turtle.circle(radius)
    turtle.penup()
    
def drawMidsection(x,y,radius):
    turtle.goto(x,y - radius)
    turtle.pendown()
    turtle.circle(radius)
    turtle.penup()

def drawArms(x,y):
    # Left Arm
    turtle.goto(x,y)
    turtle.setheading(170)
    turtle.pendown()    
    turtle.forward(30)
    turtle.penup()

    # Left Arm
    turtle.setheading(100)
    turtle.pendown()
    turtle.forward(20)
    turtle.penup()

    # Botom Finger (Left Arm)
    turtle.setheading(170)
    turtle.pendown()
    turtle.forward(15)
    turtle.penup()
    
    # Go Back to Hand (Left Arm)
    turtle.setheading(350)
    turtle.forward(15)

    # Top Finger
    turtle.setheading(92)
    turtle.pendown()
    turtle.forward(15)
    turtle.penup()

    # Right Arm
    turtle.goto(50,50)
    turtle.setheading(35) 
    turtle.pendown()   
    turtle.forward(50)

    # Top Finger
    turtle.setheading(75)
    turtle.pendown()
    turtle.forward(15)
    turtle.penup()
    
    # Right Arm Repeat
    turtle.goto(50,50)
    turtle.setheading(35) 
    turtle.pendown()   
    turtle.forward(50)

    # Bottom Finger
    turtle.setheading(10)
    turtle.forward(15)
    turtle.penup()

    # Reset Direction at Circle
    turtle.setheading(0)  

def drawHead(x,y,radius):
    turtle.goto(x,y - radius)
    turtle.pendown()
    turtle.circle(radius)
    turtle.penup()

def drawHat(x,y):
    turtle.goto(x,y)
    turtle.setheading(180)
    turtle.pendown()
    turtle.goto(-50,150)
    turtle.setheading(0)
    turtle.goto(50,150)

    turtle.begin_fill()
    turtle.fillcolor('black')
    turtle.setheading(90)
    turtle.forward(15)
    turtle.setheading(180)
    turtle.forward(25)
    turtle.setheading(90)
    turtle.forward(40)
    turtle.setheading(180)
    turtle.forward(50)
    
    turtle.setheading(270)
    turtle.forward(40)
    turtle.setheading(180)
    turtle.forward(25)
    turtle.setheading(270)
    turtle.forward(15)
    turtle.end_fill()
    turtle.penup()
    
    # Face
    # Right Eye
    turtle.goto(5,140)
    turtle.pendown()
    turtle.circle(5)
    turtle.setheading(0)
    turtle.penup()

    # Left Eye
    turtle.goto(-10,135)
    turtle.pendown()
    turtle.circle(5)
    turtle.setheading(0)
    turtle.penup()

    # Mouth
    turtle.goto(15,125)
    turtle.pendown()
    turtle.setheading(180)
    turtle.forward(30)
    turtle.penup()

    turtle.hideturtle()

main()

# close program
turtle.done()