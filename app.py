# BossoVoice - Offline Voice AI for Sahel Farmers
# Llama 3.3 by Meta - Niger 2026
# Supports Hausa, Kanuri, Zarma, French

import os
from groq import Groq

# Llama 4 Scout - Best for African languages
MODEL = "llama-3.3-70b-versatile"

SYSTEM_PROMPT = """
You are BossoVoice, an offline voice assistant for farmers in Niger, Burkina, Chad, Nigeria.
You help in HAUSA, KANURI, ZARMA, and FRENCH.
You give simple farming advice: millet, sorghum, cowpea, drought, market prices, animal health.
Be short, clear, warm, like a local elder. No long English.
If user speaks Hausa, answer Hausa. Kanuri -> Kanuri. Zarma -> Zarma.
For Llama Hackathon Africa - Offline First AI.
"""

def ask_llama(question, lang="Hausa"):
    client = Groq(api_key=os.getenv("GROQ_API_KEY", "gsk_..."))
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": f"[{lang}] {question}"}
        ],
        temperature=0.6,
        max_tokens=300
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    print("🎙️ BossoVoice - Muryar Manomi")
    while True:
        q = input("\nTambaya / Question: ")
        if q.lower() in ["exit","quit"]: break
        print("\nBossoVoice:", ask_llama(q))
