from weapon import Weapon

class Player:
    def __init__(self, name: str, max_health: int, strength: int, dexterity: int, weapon: Weapon):
        self.__name = name
        self.__max_health = max_health
        self.__health = max_health
        self.__strength = strength
        self.__dexterity = dexterity
        self.__weapon = weapon

    def get_name(self) -> str:
        return self.__name
    
    def get_health(self) -> int:
        return self.__health
    
    def set_health(self, value: int) -> None:
        self.__health = value
    
    def get_weapon(self) -> Weapon:
        return self.__weapon

    def equip(self, weapon: Weapon) -> None:
        self.__weapon = weapon

    def modifier(self, value: int) -> int:
        return (value - 10) // 2
    
    def is_alive(self) -> bool:
        return self.__health > 0
    
    def take(self, damage: int) -> int:
        if damage >= self.__health:
            damage = self.__health
        self.__health -= damage
        return damage
    
    def attack(self, enemy: "Player") -> int:
        damage = self.__weapon.get_damage()
        if self.__weapon.get_type() == "melee" or self.__weapon.get_type() == "Melee":
            damage += self.modifier(self.__strength)
        if self.__weapon.get_type == "ranged" or self.__weapon.get_type == "Ranged":
            damage += self.modifier(self.__dexterity)
        if damage < 0:
            damage = 0
        enemy.take(damage)
        return damage
    
    def __str__(self):
        return f"{self.__name} (HP: {self.__health}/{self.__max_health}, Strength: {self.__strength}, Dexterity: {self.__dexterity})"
    
