"""
Generate a random number between 1 and 9 (including 1 and 9). 
Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right. 
(Hint: remember to use the user input lessons from the very first exercise)

Extras:

Keep the game going until the user types “exit”
Keep track of how many guesses the user has taken, and when the game ends, print this out.
"""

import random 
import os

""" Created by jeroen on 28-11-2017 """


""" Main game function """
def game():
    clear()
    
    # Generate a random number
    random_number = random.randint(1,9)

    guesses = 0

    # Let the user guess a number until he/she guessed the right number
    # The game exits if the user types "exit"
    while(True):
        while(True):
            # Check if user input isn't nothing
            user_guess = input('Guess a number between 1 and 9. Type "exit" to exit the game\n> ').lower()
            if user_guess != "":
                break
            else:
                clear()
                print("Invalid input please try again")
        
        # If user input is exit close the game
        if user_guess == "exit":
            break
        
        # If the program can't convert the user input to an int
        # Then tell the user that the input is invalid
        try:
            if int(user_guess) > random_number:
                clear()
                print("Too High!")
                guesses += 1
            if int(user_guess) < random_number:
                clear()
                print("Too Low!")
                guesses += 1
        except ValueError:
            clear()
            print("Invalid input please try again..")
        
        else:
            clear()
            print("You guessed it after {} guesses!\nThe number was {}!\n".format(guesses, random_number))
            play_again = input("Do you want to play again? (Y/n)\n> ").lower()
            if play_again == "n":
                break
            else:
                game()

"""
Clear the screen
"""
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

game()