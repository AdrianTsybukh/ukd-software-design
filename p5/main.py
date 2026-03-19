from warrior import Warrior
from mage import Mage
from shaman import Shaman
from game_session import GameSession

if __name__ == "__main__":
    player1 = Warrior("Garrosh", [25, -10, 0, 40, -5, 20])
    player2 = Mage("Jaina", [35, 0, -20, 50])
    player3 = Shaman("Thrall", [0, -5, 15, 0, 10, 0, 0])

    session = GameSession("Session_001")
    session.add_participant(player1)
    session.add_participant(player2)
    session.add_participant(player3)

    for player in session._participants:
        player.check_basic_achievements()

    session.assign_mvp()
    session.generate_report("session_report.txt")
