# Python calculator

operator = input("Enter operator (* / + -): ")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if operator == "*":
    print(round(num1 * num2))
elif operator == "/":
    print(round(num1 / num2))
elif operator == "+":
    print(round(num1 + num2))
elif operator == "-":
    print(round(num1 - num2))
else:
    print(f"Invalid operator: '{operator}'. Please try again.")