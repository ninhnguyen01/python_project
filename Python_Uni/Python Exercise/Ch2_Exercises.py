# Programming Exercises (Title)

# 1. Personal Information
name = input('Enter your name: ')
address = input('Enter your address: ')
telephone_number = input('Enter your number: ')
college_major = input('Enter your major: ')


# 2. Sales Prediction
total_sales = input('Enter the projected amount of total sales: ')
profit = total_sales * 0.23
print(profit)

# 3. Land Calculation
acre = 43,560
square_feet = input('Enter the total square feet in a land: ')
total_acre = square_feet / acre
print(total_acre)

# 4. Total Purchase (error)
item_price = float(input('Enter the price for each item: '))
sub_total = item_price
sales_tax = .07
total = sub_total * sales_tax
print(total)

# 5. Distance Traveled

speed = 70          # speed in miles per hour
time = int(input('Enter the time in hours (6,10,or 15): '))
distance = speed * time
print(distance)

# 6. Sales Tax
state_sales_tax = 0.05
county_sales_tax = 0.025
total_sales_tax = state_sales_tax + county_sales_tax 

purchase = float(input('Enter the amount of purchase: '))
purchase_sales_tax = purchase * total_sales_tax
total_of_sale = purchase + purchase_sales_tax
print(total_of_sale)

# 7. Miles-per-Gallon
Milesdriven = float(input('Enter the amount of miles driven: '))
Gallonsofgasused = float(input('Enter the amount of gallons: '))
mpg = Milesdriven / Gallonsofgasused
print(mpg)

# 8. Tip, Tax, and Total
tip_percentage = 0.18
sales_tax_percentage = 0.07
meal_subtotal = float(input('Enter the total charge for food: '))
meal_tip = meal_subtotal * tip_percentage
meal_salestax= meal_subtotal * sales_tax_percentage
meal_total = meal_subtotal + meal_tip + meal_salestax 
print(meal_total)

# 9. Celsius to Fahrenheit Temperature Converter
Celsius = float(input('Enter a temperature in Celsius: '))
Fahrenheit = (9 * Celsius)/5 + 32
print(Fahrenheit)

# 10. Ingredient Adjuster
sugar = 1.5 
butter = 1
flour = 2.75
cookies = 48
num_Cookies = int(input('Enter number of cookies you want:'))
num_Sugar = (num_Cookies/cookies)*sugar
num_Butter = (num_Cookies/cookies)*butter
num_Flour = (num_Cookies/cookies)*flour
Cookies = ('You need ' + str(num_Sugar) + ' cups of sugar ' + 
str(num_Butter) + ' cups of butter, and ' + str(num_Flour) + 
' cups of flour.')
print(Cookies)

# 11. Male and Female Percentages
males = int(input('Enter the number of males: '))
females = int(input('Enter the number of females: '))

total = males + females

percent_male = males / total
percent_females = females / total

print(f'percent males:{percent_male:.0%}')
print(f'percent females:{percent_females:.0%}')

# 12. Stock Transaction Program
shares_purchased = 2000
price_per_share = 40.00
money_paid = shares_purchased * price_per_share
commission_fee = 0.03
commission_paid = (shares_purchased * price_per_share) * commission_fee
total_paid = money_paid + commission_paid

shares_sold = 2000
price_per_share_sold = 42.75
money_paid2 = shares_sold * price_per_share_sold
commission_fee2 = 0.03
commission_paid2 = (shares_sold * price_per_share) * commission_fee2
total_paid2 = money_paid2 + commission_paid2

total_money = total_paid2 - total_paid
print(total_money)

# 13. Planting Grapevines (error)
R = int(input('Enter the length of row, in feet: '))
E = int(input('Enter the amount of space, in feet: '))
S = int(input('Enter the amount of space between the vines, in feet: '))

V = (R - 2(E)) // S

# 14. Compound Interest (error)
P = float(input('Enter original principal deposited: '))
r = float(input('Enter the annual interest rate (NO DECIMAL): '))
n = int(input('Enter number of times per year that the interest is compounded: '))
t = int(input('Enter the specified number of years: '))
A = P((1 + r) /n )**n*t

# 15. Turtle Graphics Drawings

# Shape Top Left (2 square)

import turtle

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

# Shape Mid left (rectangle)

import turtle

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

# Shape Bottom Left (circle center)

import turtle

turtle.showturtle()
turtle.penup()
turtle.goto(0,-50)
turtle.pendown()
turtle.circle(50)
turtle.penup()
turtle.home()
turtle.hideturtle()

# Shape Top Right (triangle)

import turtle

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

# Shape Mid Right (five circle)

import turtle

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

# Shape Bottom Right (square)

import turtle

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

# End