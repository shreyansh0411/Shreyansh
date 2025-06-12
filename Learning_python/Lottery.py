# Making a lottery game through python

import random

computer_choice = random.randint(1,101)
user_choice = int(input("Enter the number : "))

if user_choice == computer_choice:
    print("Congratulatons 🎉 Your lotto number worked")
    print(f"Numebr was {computer_choice}")

else:
    print("Oh ☹️! Better luck next time")
    print(f"Numebr was {computer_choice}")
    