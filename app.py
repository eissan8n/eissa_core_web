from flask import Flask, render_template, request
import json

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
    brain = load_brain()
    mode = detect_complexity(user_input)

    if mode == "simple":
        return f"{user_input}\n\n(Quick Answer)\n\nCreated by Eissa Aly | عيسى علي"
    else:
        return f"{brain}\n\nUser Request:\n{user_input}\n\nFinal Answer:\n(Deep intelligent response here)\n\nCreated by Eissa Aly | عيسى علي"

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
