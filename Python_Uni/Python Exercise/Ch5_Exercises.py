# Programming Exercises (Title)

# 1 Kilometer Converter 
distance = int(input('Enter distance in kilometer: '))

def distance_convert():
    conversion = 0.6214
    miles = distance * conversion    
    print(f'{miles:.1f}')

distance_convert()

# 2 Sales Tax Program Refactoring
purchase = float(input('Enter the amount of purchase: '))

def sales_tax():
    state_sales_tax = 0.05
    county_sales_tax = 0.025
    total_sales_tax = state_sales_tax + county_sales_tax
    purchase_sales_tax = purchase * total_sales_tax
    total_of_sale = purchase + purchase_sales_tax
    print(total_of_sale)
    
sales_tax()

# 3 How Much Insurance? 
cost = float(input('Enter the replacement cost for the building: '))

def estimate():
    insurance = cost * 80 /100
    print(f'Minimum recommended insurance: {insurance} ')

estimate() 

# 4 Automobile Costs
car_loan = float(input('Enter loan cost: '))
car_insurance = float(input('Enter insurance cost: '))
car_gas = float(input('Enter gas cost: '))
car_oil = float(input('Enter oil cost: '))
car_tire = float(input('Enter tire cost: '))
car_maintenance = float(input('Enter maintenance cost: '))
 
def cost():
    monthly_auto_cost = car_loan + car_insurance + car_gas + car_oil + car_tire + car_maintenance
    print(monthly_auto_cost)
    annual_cost = monthly_auto_cost * 12
    print(annual_cost)

cost()

# 5 Property Tax
actual_val = float(input("Enter the property's actual value: "))

def property_val():
    assess_val = actual_val * 60 / 100
    property_tax = (assess_val / 100) * 0.72
    print(assess_val)
    print(f'{property_tax:.2f}')

property_val()

# 17 Prime Numbers
n = int(input("Enter an integer:")) 
def is_prime(n): 
	if n == 2: 
		return True 
	for x in range (2, n-1): 
		if n % x == 0: 
			return False 
	return True

print(is_prime(n))

# 18 Prime Number List
def is_prime(n):
    s = True
    if n < 2:
        s = False
    else:
        for i in range(2,n):
            if n % i == 0:
                s = False
    return s

for n in range(1,101):
    if is_prime(n):
        if n==97:
            print(n)
        else:
            print(n)

# 19 Future Value
def savings():  
    p = float(input("Enter current bank balance:")) 
    i = float(input("Enter interest rate:")) 
    t = float(input("Enter the amount of time that passes:")) 
    total = p * (1 + i)**t
    print(f'{total:.2f}')

savings()

# 22 Turtle Graphics: Triangle Function
import turtle
turtle.showturtle()
turtle.penup()

def triangle():
    coord_1()
    coord_2()
    coord_3()
   
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

turtle.done()

# 23 Turtle Graphics: Modular Snowman
import turtle
turtle.showturtle()
turtle.penup()
turtle.speed(0)

def main():
    drawBase(0,-75,75)
    drawMidsection(0,50,50)
    drawArms(-50,50)
    drawHead(0,130,30)
    drawHat(0,150)

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

turtle.done()

# 24 Turtle Graphics: Rectangular Pattern (incomplete)
import turtle
turtle.showturtle()
turtle.penup()
turtle.speed(0)

def drawPattern():
    drawPattern_cen()
    drawPattern_mid()
    drawPattern_out()

def drawPattern_cen():
    width = int(input('Enter the width of the pattern: '))
    height = int(input('Enter the height of the pattern: '))
    
    turtle.penup()
    turtle.goto(0,100)
    turtle.fillcolor('black')
    turtle.pendown()
    turtle.begin_fill()
    for center in range (4):
        turtle.forward(width)
        turtle.right(90)
        turtle.forward(height)
    turtle.end_fill()
    turtle.penup()

def drawPattern_mid():
    width = int(input('Enter the width2 of the pattern: '))
    height = int(input('Enter the height2 of the pattern: '))
    turtle.goto(0,150)

    for mid in range (4):
        turtle.pendown()
        turtle.forward(width)
        turtle.right(90)
        turtle.forward(height)
        turtle.penup()

def drawPattern_out():
    width = int(input('Enter the width3 of the pattern: '))
    height = int(input('Enter the height3 of the pattern: '))
    turtle.goto(0,200)

    for outer in range (4):
        turtle.pendown()
        turtle.forward(width)
        turtle.right(90)
        turtle.forward(height)
        turtle.penup()

drawPattern()

turtle.done()
