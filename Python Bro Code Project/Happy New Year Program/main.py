# Import package
import time

# Countdown statement before loop
print("Begin countdown!")
print()

# Loop for countdown
for x in reversed(range(1,11)):
    time.sleep(1) # Delay between each iteration
    print(x)
    if x == 1:
        print("Happy New Year! 🎉🎆🥳🎇🎊")