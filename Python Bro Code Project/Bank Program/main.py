# Python Bank Program

def show_balance(balance):
    print(f'Your balance is ${balance:.2f}')
    print()

def deposit():
    amount = float(input("Enter deposit amount: "))
    if amount < 0:
        print('Invalid entry!')
        print()
        return 0
    else:
        return amount   

def withdraw(balance):
    amount = float(input("Enter withdraw amount: "))
    if amount > balance:
        print('Insufficient fund!')
        print()
        return 0
    elif amount < 0:
        print('Invalid entry!')
        print()
        return 0
    else:
        return amount   

def main():
    balance = 1000.00
    is_running = True

    while is_running:
        print()
        print("Welcome to Bank!")
        print()
        print("1. Show balance")
        print("2. Deposit balance")
        print("3. Withdraw")
        print("4. Exit")
        print()
        
        choice = input("Please select an option (1-4): ")

        if choice == '1':
            show_balance(balance)
        elif choice == '2':
            balance += deposit()
        elif choice == '3':
            balance -= withdraw(balance)
        elif choice == '4':
            is_running = False
        else:
            print()
            print("Please select an option (1-4) again: ")
            print()
    
    print()
    print('Thank you for being a valued customer! Please come again!')
    print()

if __name__ == '__main__':
    main()