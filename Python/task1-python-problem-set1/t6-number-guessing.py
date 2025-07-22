import random

def number_guessing_game():
    number_to_guess = random.randint(1, 100)
    attempts = 7
    current_attempt = 1

    print("Guess the number between 1 and 100 (You have 7 attempts)")

    while current_attempt <= attempts:
        user_input = input("Attempt " + str(current_attempt) + ": Enter your guess: ")

        if not user_input.isdigit() or int(user_input) < 1 or int(user_input) > 100:
            print("Invalid input! Please enter an integer between 1 and 100.")
            continue

        guess = int(user_input)

        if guess < number_to_guess:
            print("Too low!")
            current_attempt += 1
        elif guess > number_to_guess:
            print("Too high!")
            current_attempt += 1
        else:
            print("Correct! You guessed the number.")
            return  

    print("You have used all attempts. The number was " + str(number_to_guess) + ".")

number_guessing_game()