from weapon import Weapon
from potion import Potion

class Player:
    def __init__(self, name: str, max_health: int, strength: int, dexterity: int):
        if name == "":
            raise ValueError("Name cannot be empty")
        self.__name = name

        if max_health <= 0:
            raise ValueError("Max health must be greater than 0")
        self.__max_health = max_health
        self.__health = max_health

        if strength <= 0:
            raise ValueError("Strength must be greater than 0")
        self.__strength = strength

        if dexterity <= 0:
            raise ValueError("Dexterity must be greater than 0")
        self.__dexterity = dexterity

        self.__weapon = None
        self.__buffs = []
        self.__potions = []

    @property
    def name(self) -> str:
        return self.__name
    
    @property
    def max_health(self) -> int:
        return self.__max_health
    
    @property
    def health(self) -> int:
        return self.__health
    
    @property
    def strength(self) -> int:
        return self.__strength
    
    @property
    def dexterity(self) -> int:
        return self.__dexterity

    @property
    def weapon(self) -> Weapon:
        return self.__weapon 
    
    @property
    def buffs(self) -> list[list]:
        return self.__buffs

    @property
    def effective_strength(self) -> int:
        total_buff = 0
        for buff in self.__buffs:
            if buff[0].lower() == "str" and buff[2] > 0:
                total_buff += buff[1]

        return self.__strength + total_buff
    
    @property
    def effective_dexterity(self) -> int:
        total_buff = 0
        for buff in self.__buffs:
            if buff[0].lower() == "dex" and buff[2] > 0:
                total_buff += buff[1]

        return self.__dexterity + total_buff
    
    @property
    def potions(self) -> list[Potion]:
        return self.__potions

    @weapon.setter       
    def weapon(self, weapon: Weapon) -> None:
        if not hasattr(weapon, "get_damage") or not hasattr(weapon, "weapon_type"):
            raise ValueError("Non-equippable item, not a valid weapon.")
        self.__weapon = weapon

    @potions.setter
    def potions(self, value: list[Potion]) -> None:
        if not isinstance(value, list):
            raise ValueError("Potions must be a list")
        
        if len(value) > 3:
            raise ValueError("A player can hold a maximum of 3 potions")
        
        for item in value:
            if not isinstance(item, Potion):
                raise ValueError("All items in potions list must be Potion instances")
        
        self.__potions = value

    def modifier(self, value: int) -> int:
        return (value - 10) // 2
    
    def is_alive(self) -> bool:
        return self.__health > 0
    
    def heal(self, amount: int) -> None:
        if not isinstance(amount, int):
            raise ValueError("Amount must be an integer")
        if amount < 0:
            raise ValueError("Amount must be non-negative")
        self.__health += amount
        self.__clamp_health()

    def add_buff(self, stat: str, amount: int, duration: int) -> None:
        if stat not in ["str", "dex"]:
            raise ValueError("Stat must be 'str' or 'dex'")
        
        buff_trovato = False
        for buff in self.__buffs:
            if buff[0] == stat:
                buff[1] += amount
                buff[2] += duration
                buff_trovato = True
                break
        
        if not buff_trovato:
            self.__buffs.append([stat, amount, duration])

    def tick_buffs(self) -> None:
        new_buffs = []
        
        for buff in self.__buffs:
            buff[2] -= 1
            if buff[2] > 0:
                new_buffs.append(buff)

        self.__buffs = new_buffs

    def use_potion(self, potion: Potion) -> dict:
        result = potion.apply_to(self)
        # rimuovo la pozione solo se è stata effettivamente usata
        if "error" not in result:
            self.__potions.remove(potion)

        return result
    
    def should_use_potion(self) -> Potion | None:
        if len(self.__potions) == 0:
            return None
        
        if self.__health / self.__max_health < 0.3:
            for potion in self.__potions:
                if potion.effect == "heal":
                    return potion
                
        if len(self.__buffs) == 0:
            if self.__weapon.weapon_type is None or self.__weapon.weapon_type.lower() == "melee":
                for potion in self.__potions:
                    if potion.effect == "buff_str":
                        return potion
            else:
                for potion in self.__potions:
                    if potion.effect == "buff_dex":
                        return potion
                    
        return None

    def __take(self, damage: int) -> int:
        if not isinstance(damage, int):
            raise ValueError("Damage must be an integer")
        if damage < 0:
            raise ValueError("Damage must be non-negative")
        if damage >= self.__health:
            damage = self.__health
        self.__health -= damage
        self.__clamp_health()

        return damage
    
    def __clamp_health(self) -> None:
        if self.__health > self.__max_health:
            self.__health = self.__max_health
        if self.__health < 0:
            self.__health = 0

    def __calculate_damage(self) -> int:
        if self.__weapon is None:
            return 0

        if self.__weapon.weapon_type.lower() == "melee" or self.__weapon.weapon_type.lower() == None:
            damage = self.modifier(self.effective_strength)
        if self.__weapon.weapon_type.lower() == "ranged":
            damage = self.modifier(self.effective_dexterity)
        damage += self.__weapon.get_damage()

        if damage < 0:
            return 0
        else:
            return damage

    def attack(self, enemy: "Player") -> int:
        damage = self.__calculate_damage()
        enemy.__take(damage)

        return damage
    
    def __str__(self):
        return f"{self.__name} (HP: {self.__health}/{self.__max_health}, Strength: {self.__strength}, Dexterity: {self.__dexterity})"
    