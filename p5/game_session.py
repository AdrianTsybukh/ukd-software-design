from character import Character

class GameSession:
    def __init__(self, session_id):
        self.session_id = session_id
        self._participants = []

    def add_participant(self, character_obj):
        if isinstance(character_obj, Character):
            self._participants.append(character_obj)
        else:
            raise TypeError("Participant must be an instance of Character")

    def assign_mvp(self):
        if not self._participants:
            return
            
        mvp = max(self._participants, key=lambda p: p.get_efficiency())
        mvp.achievements.add("MVP")


    def generate_report(self, filename):
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(f"--- Game Session Report: {self.session_id} ---\n")
            sorted_participants = sorted(self._participants, key=lambda p: p.get_efficiency(), reverse=True)
            
            for player in sorted_participants:
                f.write(f"""
Character: {player.name}
Status: Alive
Achievements: {", ".join(sorted(player.achievements)) if player.achievements else "None"}
Efficiency: {player.get_efficiency()}
---------------------------
""")
