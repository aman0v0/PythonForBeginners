# Number Guessing Game
import random

def number_guessing_game():
    target_number = random.randint(1, 100)
    attempts = 0

    while True:
        user_guess = int(input("Enter your guess (1-100): "))
        attempts += 1

        if user_guess == target_number:
            print(f"Congratulations! You guessed the correct number in {attempts} attempts.")
            break
        elif user_guess < target_number:
            print("Try higher.")
        else:
            print("Try lower.")

# Example usage
number_guessing_game()