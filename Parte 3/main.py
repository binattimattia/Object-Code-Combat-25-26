from player import Player
from weapon import Weapon
from potion import Potion
from random import randint

def create_weapon(player: Player) -> Weapon:
    if player.strength > player.dexterity:
        weapon_name = "Sword"
        weapon_type = "Melee"
    else:
        weapon_name = "Bow"
        weapon_type = "Ranged"

    weapon = Weapon(weapon_name, randint(5, 10), randint(11, 15), weapon_type)

    return weapon

def create_potions(player: Player) -> list[Potion]:
    potions = []
    for _ in range(2):
        heal_potion = Potion("Healing Draught", "heal", amount=10, duration=0)
        potions.append(heal_potion)
    if player.strength >= player.dexterity:
        buff_potion = Potion("Ogre Tonic", "buff_str", amount=2, duration=3)
        potions.append(buff_potion)
    else:
        buff_potion = Potion("Cat's Grace", "buff_dex", amount=2, duration=3)
        potions.append(buff_potion)
    
    return potions

def main():
    round_number = 0

    # Create Players    
    player_1 = Player("Amine", randint(80, 100), randint(1, 20), randint(1, 20))

    player_1_weapon = create_weapon(player_1)
    player_1.weapon = player_1_weapon

    player_1_potions = create_potions(player_1)
    player_1.potions = player_1_potions
    
    player_2 = Player("Cristopher", randint(80, 100), randint(1, 20), randint(1, 20))

    player_2_weapon = create_weapon(player_2)
    player_2.weapon = player_2_weapon

    player_2_potions = create_potions(player_2)
    player_2.potions = player_2_potions

    print(player_1, end=" -> ")
    print(player_1.weapon)
    print(player_2, end=" -> ")
    print(player_2.weapon)

    while player_1.is_alive() and player_2.is_alive():
        round_number += 1
        print(f"\n--- Round {round_number} ---")

        potion = player_1.should_use_potion()
        if potion is not None:
            result = player_1.use_potion(potion)
            if "error" not in result:
                print(f"{player_1.name} uses {potion.name}: {result}")

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
        
        potion = player_2.should_use_potion()
        if potion is not None:
            result = player_2.use_potion(potion)
            if "error" not in result:
                print(f"{player_2.name} uses {potion.name}: {result}")

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

        player_1.tick_buffs()
        player_2.tick_buffs()
        
if __name__ == "__main__":
    main()