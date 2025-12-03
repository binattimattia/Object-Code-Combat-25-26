class Potion:
    def __init__(self, name: str, effect: str, amount: int, duration: int):
        if len(name) > 0:
            self.__name = name
        else:
            raise ValueError("Potion name cannot be empty.")
        
        if effect.lower() in ["heal", "buff_str", "buff_dex"]:
            self.__effect = effect
        else:
            raise ValueError("Invalid potion effect. Must be 'heal', 'buff_str', or 'buff_dex'.")
        
        if amount >= 1:
            self.__amount = amount
        else:
            raise ValueError("Potion amount must be at least 1.")
        
        if duration >= 0:
            self.__duration = duration
        else:
            raise ValueError("Potion duration cannot be negative.")
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
        if self.__amount > 0:
            if self.__effect == "heal":
                if target.health == target.max_health:
                    ValueError("Target is already at maximum health.")
                self.__apply_heal(target)
                return {"effect":"heal", "amount": self.__record_amount, "duration": self.__duration}
            elif self.__effect == "buff_str":
                if target.buffs:
                    ValueError("Target already has active buffs.")
                self.__apply_buff(target, "str")
                return {"effect": self.__effect, "amount": self.__record_amount, "duration": self.__duration}
            elif self.__effect == "buff_dex":
                if target.buffs:
                    ValueError("Target already has active buffs.")
                self.__apply_buff(target, "dex")
                return {"effect": self.__effect, "amount": self.__record_amount, "duration": self.__duration}
        else:
            return {"error": "already_consumed"}
        
    def __apply_heal(self, target: "Player") -> None | dict:
        if hasattr(target, "heal") and callable(getattr(target, "heal")):
            target.heal(self.__amount)
            self.__record_amount = self.__amount
            # azzero amount per dire che la pozione è stata usata
            self.__amount = 0
        else:
            return {"error": "unsupported_target"}

    def __apply_buff(self, target: "Player", stat: str) -> None | dict:
        if hasattr(target, "add_buff") and callable(getattr(target, "add_buff")):
            target.add_buff(stat, self.__amount, self.__duration)
            self.__record_amount = self.__amount
            # azzero amount per dire che la pozione è stata usata
            self.__amount = 0
        else:
            return {"error": "unsupported_target"}
        
    def __str__(self) -> str:
        if self.__effect == "heal":
            return f"Potion({self.__effect} +{self.__amount})"
        else:
            return f"Potion({self.__effect} +{self.__amount} x{self.__duration}t)"
        