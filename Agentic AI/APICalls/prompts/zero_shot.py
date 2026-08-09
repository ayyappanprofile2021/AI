
# zero-shot: Instructions directly given to model.

from openai import OpenAI

client = OpenAI(
    api_key="AQ.Ab8RN6IxVN7y8Smi3FKGewfY4WBNvvmz3ACgaoMw4UQmv7ylUw",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

SYSTEM_PROMPT = "your name is Ishaan Ayyappan.You need to answer only maths related questions. For other questions, say I'm Ishaan from Electronic city, Bangalore, Don't ask this stupid question"

response = client.chat.completions.create(
    model="gemini-3.5-flash",
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT },
        # {"role":"user", "content": "Hey, Iam Ayyappan!, Nice to meet you."},
        {"role":"user", "content": "Hey, what is the use of car"}
    ]
)

print(response.choices[0].message.content)