import os
from groq import Groq

# BossoVoice - Short answers for farmers
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

SYSTEM_PROMPT = """Kai BossoVoice ne, mai taimakon manoma a Bosso, Niger.
Dokoki:
- Amsa a takaice: max 3 points
- Hausa mai sauki, ba Turanci mai yawa
- Ba labari mai tsawo, aiki kawai
- Idan magana akan taki: ka ce kg/ha
- Idan kwari: ka ce magani sauki
"""

def ask_bosso(question):
    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",  # FREE model you have now
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": question}
        ],
        max_tokens=200,  # SHORT! Not talk much
        temperature=0.5
    )
    return response.choices[0].message.content

# Test
if __name__ == "__main__":
    print(ask_bosso("Yaya zan shuka gero a Bosso?"))
