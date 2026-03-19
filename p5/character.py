from typing import List

class Character:
    def __init__(self, name: str, actions: List):
        self.name = name
        self.__actions = actions.copy()
        self.achievements = set()

    @property
    def actions(self):
        return list(self.__actions)

    def get_efficiency(self) -> int:
        positive = sum(a for a in self.__actions if a > 0)
        negative = sum(abs(a) for a in self.__actions if a < 0)
        return positive - negative
        
    def add_action(self, action_value: int):
        self.__actions.append(action_value)


    def get_damage_dealt(self):
        return sum(damage for damage in self.__actions if damage > 0)


    def get_damage_taken(self):
        return sum(abs(damage) for damage in self.__actions if damage < 0)


    def get_efficiency(self):
        return sum(self.__actions)


    def check_basic_achievements(self):
        damage_dealt = self.get_damage_dealt()
        damage_taken = self.get_damage_taken()
        
        if damage_dealt > 50:
            self.achievements.add("Berserker")
        
        if damage_taken > 20:
            self.achievements.add("Tank")
            
        if damage_taken == 0:
            self.achievements.add("Lucky")

