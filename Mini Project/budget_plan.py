print()
current_budget = float(input("Enter your budget: "))

def print_remaining_budget(budget):
    print("Your remaining budget is: $" + str(budget))
print_remaining_budget(current_budget)

def deduct_expense(budget,expense):
    return budget - expense

print()
expense = float(input("Enter your expense: "))
print()
new_budget = deduct_expense(current_budget,expense)
print_remaining_budget(new_budget)
print()