# Perfect Guess

import random

# Rules
print("🎮 Welcome to the Perfect Guessing Game 🎮")
print("""
📜 Rules:
1. The computer has selected a random number between 1 and 100.
2. You have to guess the number.
3. After each guess, you will be told if the number is higher or lower.
4. Type 'exit' anytime to quit the game.
Good luck! 🍀
""")

# Variables
computer_num = random.randint(1,100)
guesses = 0

# Looping Statements
while True:
    user_input = input("Enter choice ('Type 'exit' to quit') : ")
    if user_input == "exit":
        print("Thanks for playing 👏")
        break

    if not user_input.isdigit():
        print("Enter a valid number or exit")

    user_choice = int(user_input)
    guesses = guesses + 1

    if user_choice > computer_num:
        print("Choose a lower number 👇")
    elif user_choice < computer_num:
        print("Choose a higher number ☝️")
    elif user_choice == computer_num:
        print("Congratulations! You Guessed it 🎉🎉")
        print(f"Your Guesses were {guesses}")
    else:
        print("Choose a number between 1 to 100")
        


