# Create the game logic for Rock, Paper, Scissors in python

# determined by three simple rules: Rock beats scissors. Scissors beat paper.Paper beats rock.

import random
import os
#  interaction in the game will be through the console (Terminal)
# os.system('cls') # for windows
os.system('clear')  # for mac and linux(here, os.name is 'posix')
# The player can choose one of the three options rock, paper, or scissors and should be warned if they enter an invalid option.
# The computer will randomly select one of the three options.
player_score = 0
computer_score = 0
options = ["rock", "paper", "scissors"]
print("Welcome to Rock, Paper, Scissors!")
while True:
    player_input = input(
        "What do you choose? Rock, Paper, or Scissors?\n").lower()
    if player_input not in options:
        print("Invalid input. Please try again.")
        continue
    computer_input = random.choice(options)
    print(f"The computer chose {computer_input}.")
    if player_input == computer_input:
        print("You tied!")
    elif player_input == "rock" and computer_input == "scissors":
        print("You win!")
        player_score += 1
    elif player_input == "scissors" and computer_input == "paper":
        print("You win!")
        player_score += 1
    elif player_input == "paper" and computer_input == "rock":
        print("You win!")
        player_score += 1
    else:
        print("You lose!")
        computer_score += 1
    play_again = input(
        "Would you like to play again? Yes or no?\n").lower()
    if play_again == "yes":
        continue
    elif play_again == "no":
        print(f"You won {player_score} times and the computer won {computer_score} times.")
        print("Thanks for playing!")
        break
    else:
        print("Invalid input. Please try again.")
        continue
# The game will last 3 rounds.

# At each round, the player must enter one of the options in the list and be informed if they won, lost, or tied with the opponent.

# By the end of each round, the player can choose whether to play again.

# Display the player's score at the end of the game.
# The minigame must handle user inputs, putting them in lowercase and informing the user if the option is invalid.
