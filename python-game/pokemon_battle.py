from pokemon_attack import attack
from choose_pokemon import pokemon_choice
import time
import os

def start_battle():

    # sets battle play condition to true in order to start the battle game loop
    battle_continue = True

    # sets each players starting health
    user_health = 100
    opponent_health = 100

    # assigns set number of potions to each player
    heal_count_user = 4
    heal_count_opponent = 4

    # prompts user to choose their pokemon, automatically assigns another pokemon to your opponent
    os.system("clear")
    chosen_pokemon = pokemon_choice()
    user_pokemon = chosen_pokemon[0]
    opponent_pokemon = chosen_pokemon[1]

    # counts down the start of the battle
    print("Get ready for battle!")
    time.sleep(1)
    print("3...")
    time.sleep(1)
    print("2...")
    time.sleep(1)
    print("1...")
    time.sleep(1)
    print("\nGO!")
    time.sleep(1.2)
    os.system("clear")

    # while loop for the whole battle mode
    while battle_continue == True:

        # sets player 1 battle loop to true until player 2 chooses a valid action
        player_1_battle = True

        # while loop for player 1 action choices
        while player_1_battle:
            
            print("\n---------------------")
            print("Player 1\n\n1. Close range attack\n2. Far range attack\n3. Heal")
            print("---------------------")

            #user input for attack choice
            attack_choice = input("\nSelect an attack: ")
            
            # player attack/health actions imported from attack.py
            if attack_choice == "1" or attack_choice == "2":
                damage_to_opponent = attack(attack_choice)
                heal_user = 0
                time.sleep(.5)
                print(f"\n{user_pokemon} is attacking...")
                time.sleep(1)
                print(f"\n{user_pokemon} dealt {damage_to_opponent} damage to {opponent_pokemon}!")
                time.sleep(1)
                player_1_battle = False

            # keeps track of potions used by player 1
            elif attack_choice == "3":
                heal_user = attack(attack_choice)
                damage_to_opponent = 0
                heal_count_user -=1

                # if opponent has no potions left, it asks for another attack choice
                if heal_count_user == 0:
                    print("\nPlayer 1 has no more potion(s) left! Choose another attack!")
                    time.sleep(1)

                # conditional to see if opponent has potions left, if TRUE, use potion
                elif heal_count_user > 0:

                    print(f"\nPlayer 1 used a potion!")
                    time.sleep(1)
                    print(f"\n{user_pokemon} is healing...")
                    time.sleep(1)
                    print(f"\n{user_pokemon} gained {heal_user} health points!")
                    time.sleep(1)
                    print(f"\nPlayer 1 has {heal_count_user - 1} potion(s) left!")
                    time.sleep(1)
                    player_1_battle = False

            # validate if user input is valid
            elif attack_choice != "1" or attack_choice != "2" or attack_choice != "3":
                print("That is not a valid choice! Try again!")

        # keeps track of the health of player 1 and player 2
        user_health = user_health + heal_user
        opponent_health = opponent_health - damage_to_opponent

        # prevents player 1 health from going above 100 health points
        if user_health > 100:
            user_health = 100

        # if player 2 health reaches 0 (doesn't allow health to go below 0), the battle loop is broken and the game is over
        if opponent_health <= 0:
            opponent_health = 0
            break

        # updates each players health after each turn
        print("----------------")
        print(f"\n{user_pokemon}'s current health is {user_health}")
        time.sleep(1.2)
        print(f"{opponent_pokemon}'s health is {opponent_health}")

        # sets player 2 battle loop to true until player 2 chooses a valid action
        player_2_battle = True

        # while loop for player 2 action choices
        while player_2_battle:
            print("\n---------------------")
            print("Player 2\n\n1. Close range attack\n2. Far range attack\n3. Heal")
            print("---------------------")
            opponent_choice = input("\nSelect an attack: ")

            # player 2 attack/health actions imported from attack.py
            if opponent_choice == "1" or opponent_choice =="2":
                damage_to_user = attack(attack_choice)
                heal_opponent = 0
                time.sleep(.5)
                print(f"\n{opponent_pokemon} is attacking...")
                time.sleep(1)
                print(f"\n{opponent_pokemon} dealt {damage_to_user} damage to {user_pokemon}!")
                time.sleep(1)
                player_2_battle = False

            # keeps track of potions used by player 2
            elif opponent_choice == "3":
                heal_opponent = attack(attack_choice)
                damage_to_user = 0
                heal_count_opponent -= 1

                # keeps track of potions used by player 2, if opponent has no potions left, it asks for another attack choice
                if heal_count_opponent == 0:
                    print("\nPlayer 2 has no more potion(s) left! Choose another attack!")
                    time.sleep(1)                    

                # conditional to see if opponent has potions left, if TRUE, use potion
                elif heal_count_opponent > 0:
                    print(f"\nPlayer 2 used a potion!")
                    time.sleep(1)
                    print(f"\n{opponent_pokemon} is healing...")
                    time.sleep(1)
                    print(f"\n{opponent_pokemon} gained {heal_opponent} health points!")
                    time.sleep(1)
                    print(f"\nPlayer 2 has {heal_count_opponent - 1} potion(s) left!") 
                    player_2_battle = False

            # validate correct user input
            elif attack_choice != "1" or attack_choice != "2" or attack_choice != "3":
                print("That is not a valid choice! Try again!")

        # keeps track of the health of player 1 and player 2
        user_health = user_health - damage_to_user
        opponent_health = opponent_health + heal_opponent

        # prevents player 1 health from going above 100 health points
        if opponent_health > 100:
            opponent_health = 100

        # if player 1 health reaches 0 (doesn't allow health to go below 0), the battle loop is broken and the game is over
        if user_health <= 0:
            user_health = 0
            break

        # updates each players health after each turn
        print("\n----------------")
        print(f"\n{user_pokemon}'s current health is {user_health}")
        time.sleep(1.2)
        print(f"{opponent_pokemon}'s health is {opponent_health}")
        time.sleep(1)

    # conditional to determine which player won the battle
    if user_health < opponent_health:
        print("-------------------------------------------------------------")
        print(f"\n{user_pokemon} has fainted!, You lost! Better luck next time!")

    else:
        print("-------------------------------------------------------------")
        print(f"\n{opponent_pokemon} has fainted! You won against your opponent!")