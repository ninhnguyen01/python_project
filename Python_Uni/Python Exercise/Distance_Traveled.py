# This program asks the user for the speed of a vehicle 
# (in miles per hour) and the number of hours it has traveled.

speed = int(input('What is the speed of the vehicle in mph?: '))
hour = int(input('How many hours has it traveled?: '))

print('Hour\tDistance Traveled')
print('-----------------------')

for time in range (1,hour+1):
    distance = time * speed     
    print(f'{time}\t        {distance}')