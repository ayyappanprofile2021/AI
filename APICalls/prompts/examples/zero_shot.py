from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()

SYSTEM_PROMPT = """
You are a python coding expert and you know completely about python.
"""

messages_history = [
    {"role": "system", "content": SYSTEM_PROMPT},
    {"role": "user", "content": "who invented python?"},
    {"role": "assistant", "content": """
    Python was created by Guido van Rossum. 
    He started working on it in the late 1980s and released the first version, 
    Python 0.9.0, in February 1991. Guido van Rossum is often referred to 
    as the "Benevolent Dictator For Life" (BDFL) of Python due to 
    his long-term involvement in its development and management.
    """},
    {"role": "user", "content": "Is he still alive?"}
]

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=messages_history
)

print("Response:", response.choices[0].message.content)