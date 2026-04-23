import requests
from flask import Flask, render_template, request
import json


def load_memory():
    try:
        with open("memory.json", "r") as f:
            return json.load(f)
    except:
        return {"users": {}}

def save_memory(data):
    with open("memory.json", "w") as f:
        json.dump(data, f, indent=2)
app = Flask(__name__)

def load_brain():
    with open("brain.txt", "r", encoding="utf-8") as f:
        return f.read()

def load_config():
    with open("config.json", "r") as f:
        return json.load(f)

def detect_complexity(text):
    if len(text.split()) < 5:
        return "simple"
    return "complex"

def think(user_input):
    API_KEY = "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"

    url = "https://openrouter.ai/api/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "openai/gpt-3.5-turbo",
        "messages": [
            {"role": "system", "content": "You are Eissa Core AI. Be smart and helpful."},
            {"role": "user", "content": user_input}
        ]
    }

    response = requests.post(url, headers=headers, json=data)

    result = response.json()

    return result["choices"][0]["message"]["content"] + "\n\nCreated by Eissa Aly | عيسى علي""

@app.route("/", methods=["GET", "POST"])
def index():
    config = load_config()
    response = ""
    if request.method == "POST":
        user_input = request.form["user_input"]
        response = think(user_input)

    return render_template("index.html", response=response, title=config["site_title"])

if __name__ == "__main__":
    app.run(debug=True)
