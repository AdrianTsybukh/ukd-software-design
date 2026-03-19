from typing import List, Dict


def generate_report(characters: List[Dict], file_path: str):
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write("--- Game Session Report ---\n")
        for char in characters:
            f.write(f"""
Character: {char['name']}
Status: Alive
Achievements: {", ".join(sorted(char["achievements"])) if char["achievements"] else "None"}
Efficiency: {char['total_score']}
---------------------------
""")
