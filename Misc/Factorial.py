number = int(input("Enter a nonnegative integer:"))
factorial = 1
for number in range(1, number + 1):
    factorial = factorial * number
print(factorial)