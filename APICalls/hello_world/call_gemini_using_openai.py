# Make the gemini model calls using openAI sdk.

from openai import OpenAI

client = OpenAI(
    api_key="AQ.Ab8RN6IxVN7y8Smi3FKGewfY4WBNvvmz3ACgaoMw4UQmv7ylUw",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

response = client.chat.completions.create(
    model="gemini-3.5-flash",
    messages=[
        {"role": "system", "content": "You are an expert in maths and you answer pnly the question related to matchs and say sorry for other questions." },
        # {"role":"user", "content": "Hey, Iam Ayyappan!, Nice to meet you."},
        {"role":"user", "content": "Hey, what is the result of 5+5"}
    ]
)

print(response.choices[0].message.content)