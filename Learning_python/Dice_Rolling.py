# Dice Rolling Simulator

import random

print("""Welcome ! Type 1 and hit enter to roll dice
      If you wish to quit type 'exit' """)

    
while True:
    user_input = input("Enter choice ('Type 'exit' to quit') : ")   
    
    if user_input == "exit":
        print("Rolling is now stopped 🛑")
        break

    if user_input == "1":
        dice = random.randint(1,6)
        print(f"🎲 {dice}🎲")
        
    
    