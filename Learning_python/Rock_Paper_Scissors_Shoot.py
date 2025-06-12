# making stone paper scissors game

import random

choices = ["stone", "paper", "scissors"]

print("Welcome to the game")
print("There are 3 choices Stone, Paper and Scissors")
print("if you wish to exit game type exit \n")


while True:
    computer_score = 0
    user_score = 0
    round_draws = 0
    
    num = int(input("Select Total numbers of Rounds (1, 3, 5, 7) : "))
    for i in range(num):
        user_choice = input(" \n Select ur choice : ").lower()

        if user_choice not in choices:
            print("Incorrect Choice")
            continue

        computer_choice = random.choice(choices)
        print(f"Computer choice : {computer_choice}")

        print(f"Your choice: {user_choice}")

        if user_choice == computer_choice:
            print("It's a draw 😂")
            round_draws = round_draws + 1

        elif (user_choice == "stone" and computer_choice == "scissors") or (user_choice == "paper" and computer_choice == "stone") or (user_choice == "scissors" and computer_choice == "paper"):
            print("Congrats ! You Won 🎉")
            user_score = user_score + 1

        else:
            print("Oh oh ! Computer won ☹️")
            computer_score = computer_score + 1
            
        print(f"""
    Computer score 🤖 = {computer_score}
    Ur Score 🙂 = {user_score}
    Rounds Draw 📍 = {round_draws}
    """)


    again = input("Wanna play again? (yes/no): ").lower()
    if again != "yes":
        print("Bye bye! 👋")
        break