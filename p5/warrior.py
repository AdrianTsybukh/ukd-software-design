from character import Character

class Warrior(Character):
    def check_basic_achievements(self):
        super().check_basic_achievements()
        damage_dealt = self.get_damage_dealt()
        if damage_dealt > 80:
            self.achievements.add("Rage Machine")
