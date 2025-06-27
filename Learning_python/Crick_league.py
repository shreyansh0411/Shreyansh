# Cricket League

import random
import time

def welcome(Cricket_League):
    print(f"\n🎮 Welcome to {Cricket_League}! 🎉")
    time.sleep(1)
    print("There are different game mode each mode consists it's own specializations..")
    time.sleep(1)
    print("You can quit anytime by typing exit.")
    time.sleep(1)
    print("Get ready for some fun...")
    time.sleep(1)
    print("Let's begin!\n")

welcome("Cricket_League")

target = random.randint(1,31)
balls = 6
score = 0

gamemode = input("Choose game mode - BEGINNER, INTERMEDIATE, VETERAN :").lower()
if gamemode == "beginner":
    print("You have 3 wickets")
elif gamemode == "intermediate":
    print("You have 2 wickets")
elif gamemode == "veteran":
    print("You have a single wicket")    
else:
    print("Sorry can't catch it type again")

print(f"You have to chase {target} runs in {balls} balls")

while balls != 0:
    
    user_command = input("Type Play to play next balls: ").lower()

    if user_command == "exit":
        print("Thanks for playing 👏")
        break
    
    runs = random.randint(1,7)
    score = score + runs
    
    if user_command == "play":
        balls = balls - 1
        if runs == 1:
            print("Took Single")
        elif runs == 2:
            print("Took Double")
        elif runs == 3:
            print("Running between the wickets its 3")
        elif runs == 4:
            print("Boundaryyy")
        elif runs == 5:
            print("Luck huhh, got boundary on wide lol")
        else :
            print("Shot boi, Its six")
            
        runs_left = target - score
        if runs_left > 0:
            print(f"Needed runs {runs_left} in {balls} balls")
        else:
            print(f"Congratulations YOU WON 🏆")

if score == target:
    print("It's a DRAW 📍")
else:
    print("Scored less, YOU LOSE 😞") 

    