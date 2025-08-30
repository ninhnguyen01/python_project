user_name = str()
password = str()

user_name = input("Enter username (or email): ")
while user_name == "":
    user_name = input("YOU MUST ENTER A USERNAME (OR EMAIL): ")

while password.lower() != "unicorn":
    password = input("Enter the password ('q' to quit): ")
    if password == "":
        password = input("YOU MUST ENTER THE CORRECT PASSWORD ('q' TO QUIT): ")
    elif password == "q":
        exit(0)
print(f'"Welcome, {user_name}!"')
