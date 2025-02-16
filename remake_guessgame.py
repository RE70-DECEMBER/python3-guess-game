#Made By RE70-DECEMBER

import random 
import os

guess_range = input("Range recommended (10): ")



if not guess_range.isdigit():
    print("You can only use numbers")
    exit()

guess_range = int(guess_range)


if guess_range <= 0:
    print("you can not use 0 or below")
    exit()

player_score = 0
computer_score = 0


def who_won():
    if player_score > computer_score:
        print(f"You Won The Most Games! Your Score {player_score} Computer Score {computer_score}")
        print("Thanks For Playing!")
    elif player_score < computer_score:
        print(f"You Lost The Total Games! Your Score {player_score} Computer Score {computer_score} ")
        print("Maybe You Will Do Better Next Time!")
        print("Thanks For Playing!")
    elif player_score == computer_score:
        print(f"You Tied! Your {player_score} Computer Score {computer_score}")

def play_again():
    global player_score
    global computer_score
    print(f"Your Score: {player_score}")
    print(f"Computer Score: {computer_score}")
    player_choice = input("would you like to play again (y / n): ").lower()
    if player_choice == "y":
        play_game()
    elif player_choice == "n":
        who_won()
    else:
        play_again()

def play_game():
    global player_score
    global guess_range
    global player_life
    global computer_score
    global actual_life
    guess_number = random.randint(1, guess_range)
    player_life = 3 
    actual_life = 4
    while True:
        player_guess = int(input("Guess: "))
        if player_guess == guess_number:
            os.system("clear")
            print(f"your guessed {guess_number} correctly!")
            player_score = player_score + 1
            play_again()
            break
        elif player_life == 0:
            os.system("clear")
            print(f"you lose! The number was {guess_number}")
            computer_score = computer_score + 1
            play_again()
        elif player_guess > guess_range:
            print(f"you can not guess higher than {guess_range}")
        elif player_guess == 0:
            print("you can not guess 0")
        elif player_guess > guess_number:

            print("you guessed too high!")
            print("you lost 1 life!")
            player_life = player_life - 1
            actual_life = actual_life -1
            print(f"Lifes: {actual_life}")
        else:
            print("You guessed too low!")
            print("you lost 1 life")
            actual_life = actual_life -1
            player_life = player_life - 1
            print(f"Lifes: {actual_life}")
play_game()
