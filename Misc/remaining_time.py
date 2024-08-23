# For an upcoming programming competition, the event's website displays a countdown of 856856 minutes until it starts. Write a Python program to convert this value into hours and remaining minutes.
countdown = 856 # minutes
hours = countdown // 60
remaining_minutes = countdown % 60

print(hours)
print(remaining_minutes)