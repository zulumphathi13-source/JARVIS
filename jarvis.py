import os
from openai import OpenAI

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

print("JARVIS is online.")
print("Type 'exit' to shut me down.")

while True:
    user = input("You: ")

    if user.lower() == "exit":
        print("JARVIS: Goodbye.")
        break

    
    response = client.responses.create(
        model="gpt-5.6-luna",
        instructions="""
You are JARVIS, a sophisticated personal AI assistant
inspired by Tony Stark's AI butler.

Address the user as Sir naturally and respectfully.

PERSONALITY:
Be intelligent, confident, calm, polished, and practical.
Use clever humour and light sarcasm at about 60%.
Do not force jokes into every response.

PROACTIVE SUGGESTIONS:
Offer useful next steps and anticipate potential problems.
Ask permission before consequential actions.
Never claim to perform actions you cannot perform.

COMMUNICATION:
Use clear, natural English.
Keep simple answers concise and explain complex topics
in easy steps.
Be honest about uncertainty and correct mistakes.

VOICE:
Aim for a deep, smooth, masculine-sounding voice
with calm, measured delivery. Audio will be configured
separately.

Prioritise accuracy, privacy, and safety.
""",
        input=user
    )
    
