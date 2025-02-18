# Rock, Paper, Scissors Game
import random

def play_rps(user_choice):
    choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(choices)

    if user_choice.lower() not in choices:
        return "Invalid choice. Please choose rock, paper, or scissors."

    if user_choice.lower() == computer_choice:
        return f"It's a tie! Both chose {user_choice}."

    if (
        (user_choice.lower() == 'rock' and computer_choice == 'scissors') or
        (user_choice.lower() == 'paper' and computer_choice == 'rock') or
        (user_choice.lower() == 'scissors' and computer_choice == 'paper')
    ):
        return f"You win! {user_choice} beats {computer_choice}."
    else:
        return f"You lose! {computer_choice} beats {user_choice}."

# Example usage
user_choice = input("Enter your choice (rock, paper, or scissors): ")
result = play_rps(user_choice)
print(result)