import os, time
from mistralai import Mistral

api_key = os.environ["MISTRAL_API_KEY"]
model = "mistral-tiny"

client = Mistral(api_key=api_key)

# Simple example
chat_response = client.chat.complete(
    model = model,
    messages = [
        {
            "role": "user",
            "content": "What is the best French cheese?",
        },
    ]
)

print(chat_response.choices[0].message.content + "\n\n")

# Temperature example
prompt = "Tell us a joke (short one)"
chat_response = client.chat.complete(
    model = model,
    messages = [
        {
            "role": "user",
            "content": prompt,
        },
    ],
    temperature = 1.5
)

print("Temperature 1.5: " + chat_response.choices[0].message.content + "\n\n")

chat_response = client.chat.complete(
    model = model,
    messages = [
        {
            "role": "user",
            "content": prompt,
        },
    ],
    temperature = 0.0
)

print("Temperature 0: " + chat_response.choices[0].message.content + "\n\n")

# Example-Shot Learning
prompt = """
Classify sentiment as 1-5 (negative to positive) in the following statements:
1. Comfortable, but not very pretty = 2
2. Love these! = 5
3. Unbelievably good! = 
4. Shoes fell apart on the second use. = 
5. The shoes look nice, but they aren't very comfortable. = 
6. Can't wait to show them off! = 
"""

chat_response = client.chat.complete(
    model = model,
    messages = [
        {
            "role": "user",
            "content": prompt,
        },
    ]
)

print("Classifications:\n\n" + chat_response.choices[0].message.content)

from utils import ChatbotMistral

cm = ChatbotMistral()

questions = ["Why is python so popular? Give me a complete answer", "Summarize in one phrase"]

for qt in questions:
    rp = cm.make_question(qt)
    print(f"\033[1m{qt}\033[0m:\n{rp}")

