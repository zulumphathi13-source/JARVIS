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
        input=user
    )

    print("JARVIS:", response.output_text)
