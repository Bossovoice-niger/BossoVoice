"""
BossoVoice - Long-running Llama Agent for Sahel
Meta Llama Hackathon 2025
"""

import time
from datetime import datetime

# Long-running agent memory
history = []

def monitor_lake():
    level = 281.5
    data = {"time": str(datetime.now()), "level": level}
    history.append(data)
    print(f"[MONITOR] Lake Chad level: {level}m - {data['time']}")
    return level

def yumbu_advice(level, lang="hausa"):
    if level < 280:
        adv = {
          "hausa": "Ruwa yayi kasa a Tafkin Chadi. Jira mako 1 kafin shuka Gero a Yumbu. Yumbu na bukatar ruwa mai yawa.",
          "kanuri": "Ngala sau yasku. Yumbu-a Gero kasu do. Fal kala.",
          "french": "Niveau bas du lac. Attendez 1 semaine pour semer Gero sur Yumbu."
        }
    else:
        adv = {
          "hausa": "Ruwa yana da kyau! Lokaci mai kyau don shuka Gero a Yumbu. Shirya filin ka yanzu.",
          "kanuri": "Ngala beri. Yumbu-a Gero fal. Kadi karmo!",
          "french": "Bon niveau! C'est le moment de semer Gero sur sol Yumbu."
        }
    return adv.get(lang, adv["hausa"])

def llama_agent(query, lang="hausa"):
    # This simulates Llama 4 reasoning
    lake_level = monitor_lake()
    answer = yumbu_advice(lake_level, lang)
    return answer

if __name__ == "__main__":
    print("=== BossoVoice Agent Started ===")
    print("Long-running agent active for Bosso farmers...")
    q = "Yaushe zan shuka Gero a Yumbu?"
    print(f"Farmer asks: {q}")
    resp = llama_agent(q, "hausa")
    print(f"BossoVoice: {resp}")
    print(f"History length: {len(history)} - Agent remembers Lake levels")
