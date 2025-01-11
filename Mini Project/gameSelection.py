# The program is in this 'main' function
def main():
    print()
    # Input ask for your name
    user = input("Enter your name: ")
    print('Hello, ' + user)
    print('Do you want to play a game?')
    print()
    # 'Yes" response will provide a list of games to select
    game_input = input('Enter yes or no: ')
    if game_input.lower() == 'yes':
        print("Make your selection: ")
        print("1. Rock, paper, scissors")
        print("2. Monopoly")
        print("3. Poker")
        print()
        decision_input = input("Enter 1, 2, or 3: ")
        # The loop condition here is to ensure a correct response from the list of options
        while decision_input not in ['1', '2', '3']:
            print("Invalid selection")
            decision_input = input("Enter 1, 2, or 3: ")     
        if decision_input == '1':
            print("You selected Rock, paper, scissors")
        elif decision_input == '2':
            print("You selected Monopoly")
        elif decision_input == '3':
            print("You selected Poker")
        else:
            print("Invalid selection")     
    else:
        print("Okay, maybe next time") # A 'no' response will print this message before program ends

if __name__ == "__main__":
    main() # Call the main function