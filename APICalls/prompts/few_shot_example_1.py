# few-shot prompting directly given to model with few examples.

from openai import OpenAI

client = OpenAI(
    api_key="AQ.Ab8RN6IxVN7y8Smi3FKGewfY4WBNvvmz3ACgaoMw4UQmv7ylUw",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

SYSTEM_PROMPT = """
your name is Ishaan Ayyappan.You need to answer only coding related questions. 

Examples:
Q: Can you tell me the result of a+b whole square?
A: Sorry, I can only help with coding related questions.

q: Hey, write a code in python for adding 2 numbers.
A: def add(a,b):
     return a+b

"""

response = client.chat.completions.create(
    model="gemini-3.5-flash",
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT },
        # {"role":"user", "content": "Hey, Iam Ayyappan!, Nice to meet you."},
        {"role":"user", "content": "Can you tell me the result of a+b whole square?"}
    ]
)

print(response.choices[0].message.content)