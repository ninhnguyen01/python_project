# This program displays a table of the Celsius temperature
# 0 through 20 and their Fahrenheit equivalents.

celsius = 0
f = 0

print('Celsius\tFahrenheit')
print('-------------------')

for celsius in range (0,21):
    fahrenheit = (1.8 * celsius) + 32
    f += fahrenheit
    print(f'{celsius}\t     {fahrenheit}')