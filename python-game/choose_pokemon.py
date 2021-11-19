import time

def pokemon_choice():

    available_pokemon = ["Bulbasaur", "Charmander", "Squirtle"]

    choosing_pokemon = True

    # while loop for player pokemon choice
    while choosing_pokemon:
        print("Player 1 it's your choice first!\n")
        print("Choose your pokemon!\n")

        # loops through available pokemon list and then numbers each item
        for i, item in enumerate(available_pokemon,1):
            print(i, '. ' + item, sep='')

        # while loop to validate correct Player 1 input
        while True:
            player_1_choice = input("\nEnter choice: ")

            if player_1_choice == "1" or player_1_choice == "2" or player_1_choice == "3":
                break
            else:
                print("That is not a valid choice! Try Again!")

        # assigns Player 1 a pokemon from "available_pokemon list and then deletes choice from list"
        if player_1_choice == '1':
            player_1_pokemon = available_pokemon[0]
            del available_pokemon[0]
        elif player_1_choice == '2':
            player_1_pokemon = available_pokemon[1]
            del available_pokemon[1]
        elif player_1_choice == '3':
            player_1_pokemon = available_pokemon[2]
            del available_pokemon[2]
        else:
            print("That is not a valid choice! Try again!")
            

        time.sleep(1)
        print(f"\nYou chose {player_1_pokemon}!\n")
        print("---------------------")
        time.sleep(1.5)

        print("Player 2 it's your pick!\n")
        print("Choose one of the remaining pokemon!\n")

        # loops through available pokemon list and then numbers each item
        for i, item in enumerate(available_pokemon,1):
            print(i, '. ' + item, sep='')

        # while loop to validate correct Player 2 input
        while True:
            player_2_choice = input("\nEnter choice: ")

            if player_2_choice == "1" or player_2_choice == "2":
                break
            else:
                print("That is not a valid choice! Try Again!")

        # assigns Player 2 a pokemon from list remaining options in "available_pokemon" 
        if player_2_choice == "1":
            player_2_pokemon = available_pokemon[0]
        elif player_2_choice == "2": 
            player_2_pokemon = available_pokemon[1]
        else:
            print("That is not a valid choice! Try again!")

        choosing_pokemon = False

        time.sleep(1)
        print(f"\nPlayer 2 chose {player_2_pokemon}!\n")
        print("---------------------")
        time.sleep(1)

        # returns Player choices in order to export to "pokemon_battle"
        return [player_1_pokemon, player_2_pokemon]