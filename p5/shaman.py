from character import Character


class Shaman(Character):
    def check_basic_achievements(self):
        super().check_basic_achievements()
        support_actions = self.actions.count(0)
        if support_actions > 3:
            self.achievements.add("Support Pillar")
