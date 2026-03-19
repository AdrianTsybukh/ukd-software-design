from typing import List, Dict

def assign_achievements(characters_data: List[Dict]):
    if not characters_data:
        return []
        
    max_efficiency = max(char["total_score"] for char in characters_data)
    
    for char in characters_data:
        achievements = set()
        actions = char.get("actions", [])
        
        damage_dealt = sum(a for a in actions if a > 0)
        damage_taken = sum(abs(a) for a in actions if a < 0)
        
        if damage_dealt > 50:
            achievements.add("Berserker")
        
        if damage_taken > 20:
            achievements.add("Tank")
            
        if damage_taken == 0:
            achievements.add("Lucky")

        if char["total_score"] == max_efficiency:
            achievements.add("MVP")

        char["achievements"] = achievements
        
    return characters_data
