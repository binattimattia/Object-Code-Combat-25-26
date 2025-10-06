from player import Player
from weapon import Weapon
from random import randint

def create_player(name: str, health: int, strength: int, dexterity: int, weapon: Weapon) -> Player:
    if strength > dexterity:
        weapon_name = "Sword"
        weapon_type = "Melee"
    else:
        weapon_name = "Bow"
        weapon_type = "Ranged"

    weapon = Weapon(weapon_name, randint(5, 10), randint(15, 25), weapon_type)

    return Player(name, health, strength, dexterity, weapon)

def main():
    round_number = 0

    player_1_name = input("Enter the name of player 1: ")
    player_1 = create_player(player_1_name, randint(80, 100), randint(1, 20), randint(1, 20), None)
    
    player_2_name = input("Enter the name of player 2: ")
    player_2 = create_player(player_2_name, randint(80, 100), randint(1, 20), randint(1, 20), None)

    print(player_1, end=" -> ")
    print(player_1.weapon)
    print(player_2, end=" -> ")
    print(player_2.weapon)

    while player_1.is_alive() and player_2.is_alive():
        round_number += 1
        print(f"\n--- Round {round_number} ---")

        player_1_damage = player_1.attack(player_2)
        print(f"{player_1.name} attacks {player_2.name} for {player_1_damage} damage.")
        if player_2.is_alive():
            print(f"{player_2.name} has {player_2.health} HP left.")
        else:
            if player_2.health < 0:
                player_2.health = 0
            print(f"{player_2.name} has {player_2.health} HP left.")
            print(f"{player_2.name} has been defeated!")
            break

        player_2_damage = player_2.attack(player_1)
        print(f"{player_2.name} attacks {player_1.name} for {player_2_damage} damage.")
        if player_1.is_alive():
            print(f"{player_1.name} has {player_1.health} HP left.")
        else:
            if player_1.health < 0:
                player_1.health = 0
            print(f"{player_1.name} has {player_1.health} HP left.")
            print(f"{player_1.name} has been defeated!")
            break
        
if __name__ == "__main__":
    main()