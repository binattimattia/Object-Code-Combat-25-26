class Potion:
    def __init__(self, name: str, effect: str, amount: int, duration: int):
        if len(name) < 0:
            raise ValueError("Potion name cannot be empty.")
        self.__name = name
        
        if not effect.lower() in ["heal", "buff_str", "buff_dex"]:
            raise ValueError("Invalid potion effect. Must be 'heal', 'buff_str', or 'buff_dex'.")
        self.__effect = effect
        
        if amount < 1:
            raise ValueError("Potion amount must be at least 1.")
        self.__amount = amount
        
        if duration < 0:
            raise ValueError("Potion duration cannot be negative.")
        self.__duration = duration
        self.__record_amount = 0  
        
    @property
    def name(self) -> str:
        return self.__name
    
    @property
    def effect(self) -> str:
        return self.__effect
    
    @property
    def amount(self) -> int:
        return self.__amount
    
    @property
    def duration(self) -> int:
        return self.__duration
    
    def apply_to(self, target: "Player") -> dict:
        if self.__amount < 0:
            return {"error": "already_consumed"}
        
        if self.__effect == "heal":
            if target.health == target.max_health:
                raise ValueError("Target is already at maximum health.")
            self.__apply_heal(target)
            return {"effect":"heal", "amount": self.__record_amount, "duration": self.__duration}
        elif self.__effect == "buff_str":
            if target.buffs:
                raise ValueError("Target already has active buffs.")
            self.__apply_buff(target, "str")
            return {"effect": self.__effect, "amount": self.__record_amount, "duration": self.__duration}
        elif self.__effect == "buff_dex":
            if target.buffs:
                raise ValueError("Target already has active buffs.")
            self.__apply_buff(target, "dex")
            return {"effect": self.__effect, "amount": self.__record_amount, "duration": self.__duration}
            
    def __apply_heal(self, target: "Player") -> None | dict:
        if not hasattr(target, "heal") and callable(getattr(target, "heal")):
            return {"error": "unsupported_target"}
        
        target.heal(self.__amount)
        self.__record_amount = self.__amount
        # azzero amount per dire che la pozione è stata usata
        self.__amount = 0

    def __apply_buff(self, target: "Player", stat: str) -> None | dict:
        if not hasattr(target, "add_buff") and callable(getattr(target, "add_buff")):
            return {"error": "unsupported_target"}
        
        target.add_buff(stat, self.__amount, self.__duration)
        self.__record_amount = self.__amount
        # azzero amount per dire che la pozione è stata usata
        self.__amount = 0
        
    def __str__(self) -> str:
        if self.__effect == "heal":
            return f"Potion({self.__effect} +{self.__amount})"
        else:
            return f"Potion({self.__effect} +{self.__amount} x{self.__duration}t)"
        