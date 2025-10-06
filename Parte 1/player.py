from weapon import Weapon

class Player:
    def __init__(self, name: str, max_health: int, strength: int, dexterity: int, weapon: Weapon):
        self.name = name
        self.max_health = max_health
        self.health = max_health
        self.strength = strength
        self.dexterity = dexterity
        self.weapon = weapon

    def equip(self, weapon: Weapon) -> None:
        self.weapon = weapon

    def modifier(self, value: int) -> int:
        return (value - 10) // 2
    
    def is_alive(self) -> bool:
        return self.health > 0
    
    def take(self, damage: int) -> int:
        if damage >= self.health:
            damage = self.health
        self.health -= damage
        return damage
    
    def attack(self, enemy: "Player") -> int:
        damage = self.weapon.get_damage()
        if self.weapon.type == "melee" or self.weapon.type == "Melee":
            damage += self.modifier(self.strength)
        if self.weapon.type == "ranged" or self.weapon.type == "Ranged":
            damage += self.modifier(self.dexterity)
        if damage < 0:
            damage = 0
        enemy.take(damage)
        return damage
    
    def __str__(self):
        return f"{self.name} (HP: {self.health}/{self.max_health}, Strength: {self.strength}, Dexterity: {self.dexterity})"
    