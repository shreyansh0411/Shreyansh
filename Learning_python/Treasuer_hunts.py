# TREASURE HUNT

print("Welcome to the Treasure Hunting game")
print('''
                                      ████████████████████████████████████████████████████████████████████████████████████████              
                              ░░░░░░░░▒▒▒▒▒▒████████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██████████████████████████████▒▒▒▒▒▒██████▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░        
                              ████████░░░░░░████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓████████▓▓████████████████░░░░░░██████░░░░░░░░░░░░████▓▓        
                            ██░░░░░░░░██████▓▓▓▓▓▓▓▓██████████████████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▓▓░░░░░░▒▒██░░░░░░██████████▓▓░░░░░░██      
                            ██░░░░░░░░████▓▓▓▓▓▓▓▓▓▓██████████████████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▓▓░░░░░░▒▒██░░░░░░██████████▓▓░░░░░░██      
                            ██░░░░░░░░██████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██████████████░░░░░░▓▓██░░░░██▓▓▓▓▓▓▓▓██████░░░░██      
                        ████░░░░░░████▓▓▓▓▓▓████████▓▓▓▓██████████████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓████░░░░░░░░██▓▓░░██████▓▓▓▓▓▓▓▓▓▓▓▓████▓▓░░████  
                        ████░░░░░░████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓████░░░░░░░░██▓▓░░████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓████░░██▓▓  
                        ██▓▓░░░░░░████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██████████████████░░░░░░░░██▒▒░░████▓▓████████▓▓▓▓▓▓██▓▓░░██▓▓  
                        ████░░░░░░████▓▓▓▓▓▓▓▓▓▓▓▓████▓▓▓▓████████████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓████░░░░░░░░██▒▒░░████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▓▓░░██▓▓  
                        ████░░░░░░████▓▓▓▓▓▓▓▓▓▓▓▓████▓▓▓▓████████████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓████░░░░░░░░██▒▒░░████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▓▓░░██▓▓  
                        ████████████████████████████████████████████████████████████████████████████████▒▒░░██████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██░░░░██
                            ██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓██████▓▓████▓▓▓▓▓▓▓▓████████░░░░██
                            ██░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓██████▓▓██▓▓▓▓▓▓▓▓▓▓████████░░░░██
                              ████▒▒░░██████████████████████████████████████████████████████████████████▒▒░░██████▓▓▓▓██████▓▓▓▓▓▓▓▓██░░░░██
                                  ████░░▓▓██████████████████████████████████████████████████████████████████░░▒▒██████▓▓▓▓▓▓▓▓▓▓▓▓▓▓██░░░░██
                                  ░░░░▒▒▒▒▒▒████▓▓▒▒▒▒▒▒▒▒▒▒▒▒██████████████████████████████▒▒██████████████▒▒▒▒▒▒████▓▓▓▓▓▓▓▓▓▓▓▓▓▓██░░░░██
                                      ██▒▒░░██▓▓▒▒░░  ░░░░░░░░▒▒▓▓▒▒▒▒████████████████████▓▓▓▓▒▒████████████████▒▒████████▓▓▓▓██▓▓▓▓██░░░░██
                                        ▒▒░░░░▒▒██████████████████░░  ░░░░░░░░░░░░▒▒████▓▓▒▒▓▓░░▒▒████████████████░░▒▒████████▓▓▓▓▓▓██░░░░██
                                        ░░▓▓██▓▓░░▒▒░░░░░░▒▒▒▒▒▒▒▒▓▓░░░░▒▒▒▒░░░░░░░░░░░░▓▓░░▒▒▒▒▒▒▓▓▓▓░░▒▒████████▓▓▒▒▒▒▒▒██████▓▓▓▓██░░░░██
                                        ▒▒▒▒██▓▓░░░░░░░░░░░░░░░░░░██▒▒░░░░▒▒░░░░      ░░▓▓██████▓▓▓▓██░░░░░░░░░░██████▒▒░░██████▓▓▓▓██░░░░██
                                ░░░░░░▒▒▒▒▒▒██▓▓░░░░░░██████░░░░░░██░░░░░░░░░░░░░░░░▒▒▒▒░░░░░░░░░░░░░░░░░░░░  ░░▒▒████████░░▒▒████████░░░░██
                            ░░░░░░░░  ▓▓░░▒▒██▓▓░░░░░░████▓▓░░░░░░██▒▒░░░░░░░░░░░░░░▒▒▒▒░░░░░░░░░░░░░░░░▒▒▒▒▒▒░░▒▒████████▒▒▒▒████████░░░░██
                            ░░░░░░▒▒▒▒▒▒▓▓▓▓████░░▓▓████████▓▓░░░░██░░░░▒▒▒▒░░░░░░░░▒▒▒▒░░░░▒▒▒▒▒▒▒▒▒▒░░░░▒▒▒▒░░░░▒▒▒▒▒▒██▓▓▒▒▒▒██████░░░░██
                        ░░░░░░░░░░░░░░▒▒▒▒░░██▓▓░░▓▓██████████░░░░██░░░░░░▒▒░░░░  ▒▒▒▒░░  ░░▒▒▒▒░░░░░░░░░░░░░░░░  ░░  ░░▒▒████▒▒██████░░░░██
                  ████████████████████████████▓▓░░░░▒▒████▓▓░░░░░░██████████████▒▒▒▒▒▒██████████████████████████████████████████████████████
                  ████▒▒▒▒▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▒▒██▓▓░░░░░░██████░░░░░░██▒▒▒▒▒▒▒▒▒▒▓▓▒▒▓▓▒▒▒▒▒▒████▒▒▒▒████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██▒▒▒▒██
                  ████░░░░░░██░░░░░░░░░░░░░░██▓▓░░░░░░██████░░░░░░██░░░░░░░░▒▒▒▒▒▒▒▒░░░░░░████░░░░████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██░░░░██
                  ██▓▓░░░░░░██░░░░░░░░░░░░░░████░░░░░░████▓▓░░░░░░██░░░░░░░░▓▓▒▒▓▓▒▒░░░░░░████░░░░████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██░░░░██
                  ██▓▓░░░░░░██▒▒▒▒▒▒▒▒▒▒▒▒▒▒████░░░░░░████▓▓░░░░░░██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░████░░░░████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██░░░░██
                  ██▓▓░░░░░░██████████████████▓▓░░░░░░████▓▓░░░░░░████████████▒▒▒▒▒▒▒▒░░░░████░░░░████████████████████████████████████░░░░██
                  ████░░░░░░██▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▓▓░░░░░░░░░░░░░░░░░░██▓▓▓▓▓▓▓▓▓▓▒▒▒▒▓▓░░░░░░████░░░░████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██░░░░██
                  ████░░░░░░██▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▓▓░░░░░░░░░░░░░░░░░░██▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒░░░░░░████░░░░██████▓▓▓▓▓▓██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██░░░░██
                  ██▓▓░░░░░░██▓▓▓▓▓▓▓▓▓▓██████████████████████████████████▓▓▒▒▒▒▒▒▒▒░░░░░░████░░░░████▓▓▓▓▓▓▓▓▓▓▓▓██████████████▓▓▓▓██░░░░██
                  ██▓▓░░░░░░██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▓▓▒▒░░░░████░░░░██████████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██░░░░██
                  ██▓▓░░░░░░██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒░░░░████░░░░████████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██░░░░██
                  ██▓▓░░░░░░██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓████████████████████▒▒▒▒░░░░░░████░░░░████▓▓▓▓▓▓▓▓▓▓▓▓██████████████▓▓▓▓██░░░░██
                  ████░░░░░░██▓▓▓▓▓▓▓▓██████████████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▓▓░░░░░░████░░░░██████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓████▓▓▓▓▓▓▓▓██░░░░██
                  ████░░░░░░██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▓▓░░░░░░████░░░░████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██░░░░██
                  ██▓▓░░░░░░██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓████████████▓▓▓▓▓▓▓▓▓▓██▓▓░░░░░░████░░░░████▓▓▓▓▓▓████████████▓▓▓▓▓▓▓▓▓▓▓▓██░░░░██
                  ██▓▓░░░░░░██▓▓▓▓▓▓▓▓▓▓▓▓████████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓████████▓▓░░░░░░████░░░░██████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▓▓██████░░░░██
                  ██▓▓░░░░░░██▓▓▓▓▓▓▓▓▓▓▓▓██████████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓████████▓▓░░░░░░████░░░░██████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▓▓██████░░░░██
                  ████░░░░░░██████████████████████████████████████████████████████▓▓░░░░░░████░░░░████████████████████████████████████░░░░██
                  ██▓▓░░░░░░██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██▓▓░░░░░░████░░░░████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██░░░░██
                  ██▓▓░░░░░░██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██▓▓░░░░░░████░░░░████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██░░░░██
            ░░░░░░░░░░░░░░▒▒██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░████░░░░░░████░░░░████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██░░░░██
          ░░▒▒░░      ░░  ░░██████████████████████████████████████████████████████████████████████████████▒▒░░░░    ░░░░  ░░▒▒██████████████
  ░░░░░░  ░░░░  ░░▒▒░░░░░░    ░░░░  ░░▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒░░░░░░░░▒▒▒▒░░░░      ░░  ░░▒▒░░░░░░
  ░░░░▒▒░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░                                                          ▒▒░░      ░░  ░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░      
  ░░▒▒░░░░      ░░░░  ▒▒░░░░░░░░░░░░▒▒▒▒                                                          ▒▒░░░░▒▒▒▒▒▒▒▒▒▒░░░░▒▒░░░░░░░░░░▒▒░░      
      ▒▒░░▒▒▒▒▒▒▒▒▒▒▒▒░░▒▒▒▒▒▒▒▒▒▒▒▒                                                                ▒▒▒▒░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒          
        ░░░░░░░░░░░░░░▒▒                                                                                ▒▒▒▒▒▒▒▒▒▒                          

''')
while True:
    print("Your mission is to find treasure by choosing different ways given.. \n")
    print("You are spawned on an island \n")
    print("You can choose to swim all over ocean orr wait for boat to come \n")

    while True:
        user_choice = input(" \n Enter your choice (swim, wait): ").lower()

        if user_choice == "swim":
            print("There are crocodiles near by swim fast or go back to island \n")
            user_choice = input("Enter (fast) to swim fast or (return) to return on island : ").lower()
            if user_choice == "fast":
                print("Game over ! You got killed by crocodiles 🐊")
                break

            elif user_choice == "return":
                print("Ahh ! wise choice, u saved yourself 🖤 \n")
                print("I can see a boat, wave ur hands to direct the boat \n")
                user_choice = input("Enter (wave) to wave ur hands : ").lower()
                if user_choice == "wave":
                    print("Boat found you, sit on boat to make u reach to lands \n")
                    user_choice = input("Enter (sit) to sit on the boat: ")
                    if user_choice == "sit":
                        print("Boat is heading towards north...")
                        print("I can see plains and a village")
                        print("It's night time better go to bed or monsters may get u killed \n")
                        user_choice = input("Enter (sleep) to sleep in villagers house or \n enter roam to suffer the night: ").lower()
                        if user_choice == "sleep":
                            print("Sleeping through this night")
                            print("Morning.. Now we need to find cartographer for treasure map")
                            user_choice = input("Enter (find) to fing the cartographer: ").lower()
                            if user_choice == "find":
                                print("Ahh ! You found it")
                                print("Now you are just two step away from finding Treasure")
                                print("Cartographer requires some logs to trade treasure map")
                                print("Get an axe and chops some trees")
                                user_choice = input("Enter (chop) to chop trees").lower()
                                if user_choice == "chop":
                                    print("You got logs, Trade fast \n")
                                    user_choice = input("Enter (trade) to trade logs : ").lower()
                                    print("Congrats ! you are just one step away from finding treasure \n")
                                    print("As per map, you need to head north ")
                                    user_choice = input("Enter (north) to head north: ").lower()
                                    if user_choice == "north":
                                        print("Congratulations, you found it 🪙🪙🪙🪙")
                         
                                    elif user_choice != "north":
                                        print("So What are doing now fishing ??....")
                                elif user_choice != "chop":
                                    print("So What are doing now fishing ??....")
                            elif user_choice != "find":
                                print("So What are doing now fishing ??....")
                        elif user_choice != "roam":
                            print("Monsters nearby stay alert")
                            print("You got killed by monster")
                            break
                    elif user_choice != "sit":
                        print("There are monsters nearby, You can get killed anytime now")
                        print("You got killed by monsters")
                        break

                elif user_choice != "wave":
                    print("You missed the boat, now wait for next boat")
                    print("There are monsters nearby, You can get killed anytime now")
                    print("You got killed by monsters")
                    break
            else:
                print("Choose (fast) or (return)")
                
        elif user_choice == "wait":
            print("I can see a boat, wave ur hands to direct the boat \n")
            user_choice = input("Enter (wave) to wave ur hands : ").lower()
            if user_choice == "wave":
                print("Boat found you, sit on boat to make u reach to lands")
                print("Boat found you, sit on boat to make u reach to lands \n")
                user_choice = input("Enter (sit) to sit on the boat")
                if user_choice == "sit":
                    print("Boat is heading towards north...")
                    print("I can see plains and a village")
                    print("It's night time better go to bed or monsters may get u killed \n")
                    user_choice = input("Enter (sleep) to sleep in villagers house or \n enter roam to suffer the night: ").lower()
                    if user_choice == "sleep":
                        print("Sleeping through this night")
                        print("Morning.. Now we need to find cartographer for treasure map")
                        user_choice = input("Enter (find) to fing the cartographer: ").lower()
                        if user_choice == "find":
                            print("Ahh ! You found it")
                            print("Now you are just two step away from finding Treasure")
                            print("Cartographer requires some logs to trade treasure map")
                            print("Get an axe and chops some trees")
                            user_choice = input("Enter (chop) to chop trees").lower()
                            if user_choice == "chop":
                                print("You got logs, Trade fast \n")
                                user_choice = input("Enter (trade) to trade logs : ").lower()
                                print("Congrats ! you are just one step away from finding treasure \n")
                                print("As per map, you need to head north ")
                                user_choice = input("Enter (north) to head north: ").lower()
                                if user_choice == "north":
                                    print("Congratulations, you found it 🪙🪙🪙🪙")
                                elif user_choice != "north":
                                        print("So What are doing now fishing ??....")
                                elif user_choice != "chop":
                                    print("So What are doing now fishing ??....")
                            elif user_choice != "find":
                                print("So What are doing now fishing ??....")
                        elif user_choice != "roam":
                            print("Monsters nearby stay alert")
                            print("You got killed by monster")
                            break
                    elif user_choice != "sit":
                        print("There are monsters nearby, You can get killed anytime now")
                        print("You got killed by monsters")
                        break

            elif user_choice != "wave":
                print("You missed the boat, now wait for next boat")
                print("There are monsters nearby, You can get killed anytime now")
                print("You got killed by monsters")
                break

        else:
            print("i repeat enter your choice(swim, wait)")
    
    play_again = input("\n Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("Thanks for playing! Goodbye 👋")
        break