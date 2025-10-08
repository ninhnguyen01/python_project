# This program displays the number of millimeters that the ocean 
# will have risen each year for the next 25 years.

ocean_lvl = 1.6 
total = 0

for o in range(1,26):
    o *= ocean_lvl
    print(f'{o:.1f}')