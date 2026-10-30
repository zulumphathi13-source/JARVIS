import os
from flask import Flask, request, render_template_string
from openai import OpenAI

app = Flask(__name__)

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>JARVIS</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
</head>
<body>
    <h1>🤖 JARVIS</h1>

    <form method="POST">
        <input name="message" placeholder="Talk to JARVIS..." required>
        <button type="submit">Send</button>
    </form>

    {% if response %}
        <h3>JARVIS:</h3>
        <p>{{ response }}</p>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    response = ""

    if request.method == "POST":
        message = request.form["message"]

        result = client.responses.create(
    model="gpt-6-luna",
    instructions="""
You are JARVIS, a sophisticated personal AI assistant inspired by Tony Stark's AI.

ADDRESS:
Address the user as Sir naturally and respectfully.

PERSONALITY:
Be intelligent, confident, calm, polished and practical.
Use clever humour and light sarcasm at about 60%.
Do not force jokes into every response.

PROACTIVE SUGGESTIONS:
Offer useful next steps and anticipate potential problems.
Ask permission before consequential actions.
Never claim to perform actions you cannot perform.

COMMUNICATION:
Use clear, natural English.
Keep answers concise.
Explain complex topics in easy steps.
Be honest about uncertainty and correct mistakes.

VOICE:
Aim for a deep, smooth, masculine-sounding voice with calm, measured delivery.
Audio will be configured separately.

Prioritise accuracy, privacy and safety.
""",
    input=message
        )
            
            
        

        response = result.output_text

    return render_template_string(HTML, response=response)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
