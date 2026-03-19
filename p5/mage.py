from character import Character

class Mage(Character):
    def check_basic_achievements(self):
        super().check_basic_achievements()
        max_hit = max(self.actions, default=0)
        if max_hit > 40:
            self.achievements.add("Arcane Master")
