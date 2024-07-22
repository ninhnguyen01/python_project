# draw circles

# import package
import turtle

# main function
def main():
    turtle.hideturtle()
    circle(0,0,100,'red')
    circle(-150,-75,50,'blue')
    circle(-200,150,75,'green')

# circle function
def circle (x,y,radius,color):
    turtle.penup()
    turtle.goto(x,y - radius)
    turtle.fillcolor(color)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()  

# Call the main function.
if __name__ == '__main__':
    main()

# close program
turtle.done()