# Programming Exercises (Title)

# 1
number = int(input('Enter a number between 1 and 7: '))

if number >= 1 and number <= 7:
    if number == 1:
        print('Monday')
    elif number == 2:
        print('Tuesday')
    elif number == 3:
        print('Wednesday')
    elif number == 4:
        print('Thursday')
    elif number == 5:
        print('Friday')
    elif number == 6:
        print('Saturday')
    elif number == 7:
        print('Sunday')
    else:
        print("You didn't enter a number between 1 and 7!")

# 2
length1 = int(input("Enter the rectangle's length: "))
width1 = int(input("Enter the rectangle's width: "))
rectangle1 = length1 * width1
length2 = int(input("Enter the rectangle's length: "))
width2 = int(input("Enter the rectangle's width: "))
rectangle2 = length2 * width2

if rectangle1 > rectangle2:
    print(rectangle1)
elif rectangle2 > rectangle1:
    print(rectangle2)
else:
    print('They are the same.')

# 3
person_age = int(input("Enter a person's age: "))

if person_age <= 1:
    print('Person is an infant.')
elif person_age > 1 and person_age < 13:
    print('Person is a child.')
elif person_age >= 13 and person_age < 20:
    print('Person is a teenager.')
else:
    print('Person is an adult.')

# 4 
number = int(input('Enter a number between 1 and 10: '))

if number == 1:
    print('I')
elif number == 2:
    print('II')
elif number == 3:
    print('III')
elif number == 4:
    print('IV')
elif number == 5:
    print('V')
elif number == 6:
    print('VI')
elif number == 7:
    print('VII')
elif number == 8:
    print('VIII')
elif number == 9:
    print('IV')
elif number == 10:
    print('X')
else:
    print("You didn't enter a number between 1 and 10!")


# 5
mass = float(input("Enter an object's mass:" ))

weight = mass * 9.8
print(weight)

newtons1 = 500
newtons2 = 100

if weight > newtons1:
    print('Object is too heavy.')

if weight < newtons2: 
        print('Object is too light.')


# 6
month = int(input('Enter a month(in nunmeric form):'))
day = int(input('Enter a day: '))
two_digit_year = int(input('Enter a two digit year: '))

two_digit_year = month * day

if month * day ==  two_digit_year:
    print('The date is magic.')
else:
    print('The date is not magic.')

# 7
primarycolor = str(input('Enter a primary color: '))
primarycolor2 = str(input('Enter a primary color: '))

if primarycolor == 'red' and primarycolor2 == 'blue':
    print(f'When you mix {primarycolor} and {primarycolor2}, you get purple.')
elif primarycolor == 'blue' and primarycolor2 == 'red':
    print(f'When you mix {primarycolor} and {primarycolor2}, you get purple.')
elif primarycolor == 'red' and primarycolor2 == 'yellow':
    print(f'When you mix {primarycolor} and {primarycolor2}, you get orange.')
elif primarycolor == 'yellow' and primarycolor2 == 'red':
    print(f'When you mix {primarycolor} and {primarycolor2}, you get orange.')
elif primarycolor == 'blue' and primarycolor2 == 'yellow':
    print(f'When you mix {primarycolor} and {primarycolor2}, you get green.')
elif primarycolor == 'yellow' and primarycolor2 == 'blue':
    print(f'When you mix {primarycolor} and {primarycolor2}, you get green.')
else: 
    print('You did not enter primary colors (red, blue, or yellow) in the correct combo!')
    
# 8 
hotdog_pak = 10
hotdogBun = 8
cookout_people = int(input('Enter the number of people attending: '))
pack_hotdog = int(input('Enter the number of packages of hotdog: '))
pack_hotdog_bun = int(input('Enter the number of packges of hotdog buns: '))

cookout_hotdog_leftover = pack_hotdog - cookout_people
print(cookout_hotdog_leftover)
cookout_hotdog_bun_leftover = pack_hotdog_bun - pack_hotdog
print(cookout_hotdog_bun_leftover)
