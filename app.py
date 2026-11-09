import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

# BossoVoice - Switch to Meta Llama API (Muse Spark)
client = OpenAI(
    api_key=os.getenv("LLAMA_API_KEY"),
    base_url="https://api.llama.com/compat/v1/"
)

SYSTEM_PROMPT = """
Kai BossoVoice ne, mai taimakon manoma a Bosso, Niger.
Dokoki:
- Amsa a takaice: max 3 points
- Hausa mai sauki, ba Turanci mai yawa
- Ba labari mai tsawo, aiki kawai
- Idan magana akan taki: ka ce kg/ha
- Idan kwari: ka ce magani sauki
- Idan ruwan sama: ka ce kwana nawa
"""

def ask_bosso(question: str, lang="hausa"):
    response = client.chat.completions.create(
        model="Llama-4-Maverick-17B-128E-Instruct-FP8",
        # or Muse Spark if you have access: "Llama-4-Maverick" / Spark
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": question}
        ],
        temperature=0.3,
        max_tokens=300
    )
    return response.choices[0].message.content

# Test
if __name__ == "__main__":
    print(ask_bosso("Yaushe ruwan sama zai yi?"))
    print(ask_bosso("When rain?", lang="kanuri"))
