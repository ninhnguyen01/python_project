# Programming Exercises (Title)

# 1 Bug Collector
MAX = 5
total_bugs = 0

for b in range(MAX):
    day_bugs = int(input('Enter the number of bugs discovered today: '))
    total_bugs += day_bugs
    print(total_bugs)

# 2 Calories Burned
cal_per_min = 4.2

for c in range (10,35,5):
    total = cal_per_min * c
    print(total)

# 3 Budget Analysis
expense = 'Y'
max_budget = 1000.00
total_budget = 0

while expense == 'Y' :
    budget = float(input('Enter your expense for the month: '))
    total_budget += budget
    print(total_budget)
    expense = str(input('Do you have more expenses to add?' +
    " If yes, enter 'Y': "))

if total_budget <= max_budget:
    print('You are under budget')
else:
    print('You are over budget!')

# 4 Distanced Traveled 
speed = int(input('What is the speed of the vehicle in mph?: '))
hour = int(input('How many hours has it traveled?: '))

print('Hour\tDistance Traveled')
print('-----------------------')

for time in range (1,hour+1):
    distance = time * speed     
    print(f'{time}\t        {distance}')

# 5 Average Rainfall
years = int(input('Enter the number of years: '))
total = 0

for year in range(1,years+1):
    for month in range(1,13):
        rainfall = float(input('Enter inches of rainfall this month: '))
        total += rainfall
        mon = years * 12
        avg = total / month
        print(month,total,avg)

# 6 Celsius to Fahrenheit Table
celsius = 0
f = 0

print('Celsius\tFahrenheit')
print('-------------------')

for celsius in range (0,21):
    fahrenheit = (1.8 * celsius) + 32
    f += fahrenheit
    print(f'{celsius}\t     {fahrenheit}')

# 7 Pennies for Pay
days = int(input('Enter the number of days: '))
total = 0

print('Day\tSalary')
print('-----------')

for s in range(days):
    salary = 2**s 
    total += salary
    print(f'{s+1}\t     {salary}')

total_pay = total / 100
print(f'total pay: ${total_pay:.2f}')

# 8 Sum of Numbers
num = 'Y'
total = 0

while num == 'Y':
    pos_num = int(input('Enter a positive number: '))
    total += pos_num 
    num = input("Enter 'Y' to continue or negative number to end: ")
    print(total)

# 9 Ocean Levels
ocean_lvl = 1.6 
total = 0

for o in range(1,26):
    o *= ocean_lvl
    print(f'{o:.1f}')

# 10 Tuition Increase
tuition = 8000
for i in range(1, 6):
	tuition *= 1.03
	if i == 1:
		print("In 1 year, the tuition will be $" + str(tuition) + ".")
	else:
		print("In "+str(i)+" years, the tuition will be $" + str(tuition) + ".")

# 11 Weight Loss (stuck) 
start_weight = float(input('Enter your starting weight: '))
monthly_loss = 4
total = 0

print("Start Weight\tEnd Weight")
print('------------------------')

for w in range (1,7):
    w = start_weight - monthly_loss
    total = w 
    print(f'{start_weight},\t       {total}') 

# 12 Calculating the Factorial of a Number
number = int(input("Enter a nonnegative integer:"))
factorial = 1
for number in range(1, number + 1):
    factorial *= number
print(factorial)

# 13 Population (missing day 1)
num = int(input('Enter starting number of organisms: '))
percent = int(input('Enter the average daily increase: '))
day = int(input('Enter the number of days: '))

print('Day Approximate\tPopulation')

for p in range (2,day+1):
        increase = num * percent / 100
        num += increase
        print(f'{p}\t        {num}')

# 14 Write a Program that uses nested loops to draw this pattern:
for x in range (7,0,-1): 
    for y in range(x):
        print('*', end = '')
    print('\n')  

# 15 Write a Program that uses nested loops to draw this pattern:
n = int(input('Enter number of lines for pattern:'))
for x in range (0,n): 
    print('#', end = '')
    for y in range(x):
	    print(' ', end = '')
print('#')

# 16 Turtle Graphics: Repeating Squares
import turtle
turtle.showturtle()
turtle.setheading(180)
turtle.penup()
turtle.goto(200,-200)
turtle.hideturtle()
turtle.pendown()
turtle.speed(0)

move = 4

for x in range (100):
    move += 4
    for y in range (4):
        turtle.forward(move)
        turtle.right(90)

turtle.done()

# 17 Turtle Graphics: Star Pattern
# Long Way (Wrong Way)
import turtle
turtle.showturtle()
turtle.penup()
turtle.goto(250,-100)
turtle.pendown()
turtle.speed(5)

for x in range (8):
        turtle.goto(-250,-100)
        turtle.goto(100,250)
        turtle.goto(100,-250)
        turtle.goto(-250,100)
        turtle.goto(250,100)
        turtle.goto(-100,-250)
        turtle.goto(-100,250)
        turtle.goto(250,-100)
        turtle.penup()
        turtle.hideturtle()

turtle.done()

# Right Way
import turtle 
turtle.showturtle()
turtle.penup()
turtle.goto(-150,-50)
turtle.pendown()
turtle.speed(5)

for x in range (8):
    turtle.forward(300)
    turtle.left(135)
    turtle.hideturtle()

turtle.done()

# 18 Turtle Graphics Hypnotic Pattern
import turtle
turtle.showturtle()
turtle.pendown()
turtle.setheading(90)
turtle.speed(10)

move = 5

for x in range (12):
    for y in range (4):
        turtle.forward(move)
        turtle.left(90)
        turtle.hideturtle()
        move += 5

turtle.done()

# 19 Turtle Graphics: STOP Sign
import turtle

turtle.showturtle()
turtle.penup()
turtle.goto(-50,100)
turtle.pendown()
turtle.speed(8)

for x in range (8):
    turtle.forward(100)
    turtle.right(45)

turtle.penup()
turtle.goto(-15,-30)
turtle.pendown()
turtle.write('STOP',font=20)
turtle.hideturtle()

turtle.done()