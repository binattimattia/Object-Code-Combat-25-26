import random

class Weapon:
    def __init__(self, name: str, min_damage: int, max_damage, weapon_type: str):
        if name == "":
            ValueError("Weapon name cannot be empty.")
        self.__name = name

        if min_damage < 1:
            ValueError("Min damage cannot be less than 1.")
        self.__min_damage = min_damage

        if max_damage < min_damage:
            ValueError("Max damage cannot be less than min damage.")
        self.__max_damage = max_damage
        
        if weapon_type.lower() not in ["melee", "ranged"]:
            ValueError("Weapon type must be either 'melee' or 'ranged'.")
        self.__weapon_type = weapon_type

    @property
    def name(self) -> str:
        return self.__name
    
    @property
    def min_damage(self) -> int:
        return self.__min_damage
    
    @property
    def max_damage(self) -> int:
        return self.__max_damage
    
    @property
    def weapon_type(self) -> str:
        return self.__weapon_type

    def get_damage(self) -> int:
        return random.randint(self.__min_damage, self.__max_damage)
