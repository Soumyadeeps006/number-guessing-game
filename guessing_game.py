import random

secret_number = random.randint(1, 100)

guesses = 0
guessed = False

while not guessed:
    try:
        user_guess = int(input("Guess a number between 1 and 100: "))
        guesses += 1

        if user_guess < 1 or user_guess > 100:
            print("Your guess is out of range! Please guess a number between 1 and 100.")
        elif user_guess < secret_number:
            print("Too low! Try again.")
        elif user_guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed it in {guesses} tries.")
            guessed = True
    except ValueError:
        print("Please enter a valid number.")