from pokemon_battle import start_battle
# import pygame
# from audio import classic_intro

def main():

    while True:

        # tried to import music (something to research and work on)
        # pygame.mixer.music.fadeout(4000)

        # imported battle mode from "pokemon_battle.py"
        start_battle()

        # while loop for game reset/game end
        while True:
            # asks user if they want to play again
            play_again = input("\nDo you want to play again? y or n? ")
            
            # create validation for correct choice
            if play_again == "y" or play_again == "yes":
                break
                
            elif play_again == "n" or play_again == "no":
                exit("\nThanks for playing my game! I hope you had as much fun as I did making it!\n")
                
            else:
                print("\nThat is an invalid choice, try again!")

main()

