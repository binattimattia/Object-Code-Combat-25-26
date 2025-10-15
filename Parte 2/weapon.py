import random

class Weapon:
    def __init__(self, name: str, min_damage: int, max_damage, type: str):
        self.__name = name
        self.__min_damage = min_damage
        if min_damage < 1:
            self.__min_damage = 1
            print("Min damage cannot be less than 1. Setting to 1.")
        if max_damage < min_damage:
            self.__max_damage = self.__min_damage + 1
            print("Max damage cannot be less than min damage. Setting max damage to min damage + 1.")
        self.__max_damage = max_damage
        self.__type = type

    def get_damage(self) -> int:
        return random.randint(self.__min_damage, self.__max_damage)
    
    def get_type(self):
        return self.__type
    
    def __str__(self):
        return f"Weapon: {self.__name} ({self.__min_damage}-{self.__max_damage} dmg)"
