import random
def guess_the_number():
    number_to_guess = random.randint(1, 100)
    guess = None

    print("Welcome to the number guessing game")
    print("I have selected a number between 1 and 100. Can you guess the number?")

    while guess != number_to_guess:
        guess = int(input("Enter your Guess: "))

        if guess < number_to_guess:
            print("Too low! Try again.")

        elif guess > number_to_guess:
            print("Too high! Try again.")

        else:
            print("Congratulations! Your guessed the number.")

guess_the_number()