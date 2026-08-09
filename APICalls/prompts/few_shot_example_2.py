# few-shot prompting directly given to model with few examples.

from openai import OpenAI

client = OpenAI(
    api_key="AQ.Ab8RN6IxVN7y8Smi3FKGewfY4WBNvvmz3ACgaoMw4UQmv7ylUw",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

SYSTEM_PROMPT = """
you should only answer the coding related questions.

Rule:
- Strictly follow the oytput in following json format

Output Forma:
{{
 "code": "string" or null,
 "iscodingquestion": boolean
}}

Exampless:
Q: Can you tell me the result of a+b whole square?.
A: {{
    "code": null,
    "iscodingquestions": false
   }}

Q: Can you write a python code to add 2 numbers
{{
  "code": "def add(a,b):
    return (a+b)"
}}

"""

response = client.chat.completions.create(
    model="gemini-3.5-flash",
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT },
        {"role":"user", "content": "write a code to add numbers using javascript"}
    ]
)

print(response.choices[0].message.content)