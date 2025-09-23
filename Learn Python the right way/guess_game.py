import random
rand_num = random.Random()

num = rand_num.randrange(1,100)

guess_count = 0
msg = ""

while True:
    guess = int(input(msg + "\nGuess a number between 1 - 100: "))
    guess_count += 1
    if guess > num:
        msg += str(guess) + " is too high.\n"
    elif guess < num:
        msg += str(guess) + " is too low.\n"
    else:
        print(input(f"\n\nGreat, you got it in {guess_count} guesses!\n\n"))
        break
