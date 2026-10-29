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
            input=message
        )

        response = result.output_text

    return render_template_string(HTML, response=response)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
