import random

def attack(attack_choice):

    # while loop for calculation Player attack choices
    while True:
        if attack_choice == "1":
            attack_points = random.randint(18,25)
            return attack_points

        elif attack_choice == "2":
            attack_points = random.randint(10,35)
            return attack_points

        elif attack_choice == "3":
            heal_points = random.randint(18,25)
            return heal_points

        return attack(attack_choice)