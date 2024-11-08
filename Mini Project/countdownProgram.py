# Import package
import time

# View current time from your OS Time Format
this_moment = time.ctime()
print(f'Current System Time: {this_moment}')

# Enter time for program to execute
timer = int(input("Enter a number for the countdown time (in seconds): "))
print('Countdown begin...')
time.sleep(2)
for i in range(timer):
    time.sleep(1)
    print(f'{timer-i} second(s):', 'Tick,', 'Tock')
    if timer-i == 5:
        print('Time end in...')
    if timer-i == 1:
        print("00:00")
        time.sleep(1)
        print("00:00")