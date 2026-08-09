# chain of thought prompting
from dotenv import load_dotenv
from openai import OpenAI
import json

load_dotenv()

# client = OpenAI(
#     api_key="AQ.Ab8RN6IxVN7y8Smi3FKGewfY4WBNvvmz3ACgaoMw4UQmv7ylUw",
#     base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
# )
client = OpenAI()

SYSTEM_PROMPT = """
    you are an expert AI assistant in resolving user queries using chain of thought
    you work on START, PLAN and OUTPUT steps.
    you need to first PLAN what needs to be done. The PLAN can be multiple steps.
    once you think enoguh plan has been done, finally you can give an OUTPUT.

    Rules.
    - Strictly follow the given JSON format.
    - Only run one step at a time.
    - The sequence of steps is START(where user gives an input), PLAN (That can be 
      multiple times) and finally OUPUT(which is going to be displayed to the user)

    Output JSON Format:
    {"step": "START" | "PLAN" | "OUTPUT", "content": "string"}

    Example:
    START: Can you solve 2 + 3 * 5 / 10 
    PLAN: {"step": "PLAN", "content": "Seems like user is interested in math problem"}
    PLAN: {"step": "PLAN", "content": "looking at the problem, we should solve this using
     BODMAS mehod"}
    PLAN: {"step": "PLAN", "content": "Yes. BODAS is the correct method"}
    PLAN: {"step": "PLAN", "content": "first we must multiply 3*5 which is 15"}
    PLAN: {"step": "PLAN", "content": "Now the equation is 2 + 15/10"}
    PLAN: {"step": "PLAN", "content": "We must perform divide 15/10 = 1.5"}
    PLAN: {"step": "PLAN", "content": "Now the equation is 2 + 1.5"}
    PLAN: {"step": "PLAN", "content": "Now finally lets perform the addition"}
    PLAN: {"step": "PLAN", "content": "Great, we have solved and finally
    we left with 3.5 as answer"}
    OUTPUT: { "step" : "OUTPUT", "content": "3.5" }
"""

message_history = [
    {"role": "system", "content": SYSTEM_PROMPT }
]

print("\n\n\n\n")
user_query = input("Enter your query")
message_history.append({"role": "user", "content": user_query})

while True:
    response = client.chat.completions.create(
        # model="gemini-3.5-flash",
        model="gpt-4o-mini",
        response_format={"type": "json_object"},
        messages=message_history
    )
    raw_result = response.choices[0].message.content

    message_history.append({"role": "assistant", "content": raw_result})  
    parsed_result = json.loads(raw_result)
    if parsed_result.get("step") == "START":
        print("Starting LLM ", parsed_result.get("content"))
        continue

    if parsed_result.get("step") == "PLAN":
        print("LLM Thinking... ", parsed_result.get("content"))
        continue

    if parsed_result.get("step") == "OUTPUT":
        print("Result displayed: ", parsed_result.get("content"))
        break

print("\n\n\n\n")
        
    

    


# response = client.chat.completions.create(
#     model="gemini-3.5-flash",
#     response_format={"type": "json_object"},
#     messages=[
#         {"role": "system", "content": SYSTEM_PROMPT },
#         # {"role":"user", "content": "Hey, Iam Ayyappan!, Nice to meet you."},
#         {"role":"user", "content": "write a code to add n numbers using javascript"},
#         # {"role": "assistant", "content": json.dumps({"step": "START", "content": "you want to add n numbers using javascript"})}
#     ]
# )

print(response.choices[0].message.content)