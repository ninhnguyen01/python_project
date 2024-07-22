males = int(input("Enter number of males:"))
females = int(input("Enter number of females:"))

total = males + females

perMales= males/total
perFemales = females/total

print(f'Percent males: {perMales:.0%}')
print(f'Percent females: {perFemales:.0%}')