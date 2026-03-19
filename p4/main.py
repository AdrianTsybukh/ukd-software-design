from typing import List, Dict
from collections import Counter
from pprint import pprint

import achievements
import reports

def analyze_numeric_data(data: List[int]) -> Dict:
    if not data:
        return {}

    return {
        "count": len(data),
        "sum": sum(data),
        "avg": sum(data) / len(data),
        "positive": len([x for x in data if x > 0]),
        "negative": len([x for x in data if x < 0]),
        "zero": len([x for x in data if x == 0]),
        "max": max(data),
        "min": min(data)
    }

def analyze_text_logs(log: str) -> Dict:
    text = log.lower().strip()
    lines = [line.strip() for line in text.splitlines() if line.strip()]

    counts = Counter(lines)

    most_frequent_event, _ = counts.most_common(1)[0] # цей метод повертає список кортежів, я беру тільки перший

    char_count = sum(len(word) for word in text.split())
    word_count = len(text.split())

    return {
        "char_count": char_count,
        "word_count": word_count,
        "player_lines": sum(1 for line in lines if line.startswith("player")),
        "enemy_lines": sum(1 for line in lines if line.startswith("enemy")),
        "most_frequent_event": most_frequent_event
    }


def get_character_efficiency(characters: List[Dict]):
    results = []
    for char in characters:
        stats = analyze_numeric_data(char["actions"])
        results.append({
            "name": char["name"],
            "actions": char["actions"],
            "avg_score": stats["avg"],
            "total_score": stats["sum"]
        })

    best_char = max(results, key=lambda x: x["total_score"])

    return results, best_char

def create_report(events_list: List[int], log_string: str, chars_data: Dict) -> Dict:
    event_stats = analyze_numeric_data(events_list)
    text_stats = analyze_text_logs(log_string)
    char_stats, winner = get_character_efficiency(chars_data)

    return {
        "event_stats": event_stats,
        "text_stats": text_stats,
        "char_stats": char_stats,
        "winner": winner
    }


events_list = [15, -8, 0, 30, -12, 5, 0, -3, 20]
log_string = """
Player1 entered the dungeon.
Player1 attacked the enemy!
Enemy attacked Player1!
Player1 used healing potion.
Player1 defeated the enemy!
Player1 exited the dungeon.
"""


if __name__ == "__main__":
    chars_data = [
        {"name": "Warrior", "actions": [25, -10, 0, 40, -5]},
        {"name": "Mage", "actions": [35, 0, -20, 50]},
        {"name": "Archer", "actions": [20, -5, 15, 0, 10]}
    ]

    char_stats, best_char = get_character_efficiency(chars_data)
    chars_with_achievements = achievements.assign_achievements(char_stats)
    filtered_chars = [char for char in chars_with_achievements if char["achievements"]]
    filtered_chars.sort(key=lambda x: x["total_score"], reverse=True)
    reports.generate_report(filtered_chars, "result.txt")
