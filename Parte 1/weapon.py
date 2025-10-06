import random

class Weapon:
    def __init__(self, name: str, min_damage: int, max_damage, type: str):
        self.name = name
        self.min_damage = min_damage
        if min_damage < 1:
            self.min_damage = 1
            print("Min damage cannot be less than 1. Setting to 1.")
        if max_damage < min_damage:
            self.max_damage = self.min_damage + 1
            print("Max damage cannot be less than min damage. Setting max damage to min damage + 1.")
        self.max_damage = max_damage
        self.type = type

    def get_damage(self) -> int:
        return random.randint(self.min_damage, self.max_damage)
    
    def __str__(self):
        return f"Weapon: {self.name} ({self.min_damage}-{self.max_damage} dmg)"
