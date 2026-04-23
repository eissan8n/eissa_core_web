from flask import Flask, render_template, request
import json
import requests

app = Flask(__name__)

# 🧠 تحميل الذاكرة
def load_memory():
    try:
        with open("memory.json", "r") as f:
            return json.load(f)
    except:
        return {"users": {}}

# 💾 حفظ الذاكرة
def save_memory(data):
    with open("memory.json", "w") as f:
        json.dump(data, f, indent=2)

# 🤖 الذكاء
def think(user_input):
    memory = load_memory()
    user_id = "default"

    if user_id not in memory["users"]:
        memory["users"][user_id] = []

    # حفظ الرسالة
    memory["users"][user_id].append(user_input)

    # آخر 5 رسائل
    history = memory["users"][user_id][-5:]

    save_memory(memory)

    # 🧠 بناء الرسائل
    messages = [
        {
            "role": "system",
            "content": """
You are Eissa Core AI.

- Think before answering
- Be intelligent and precise
- Use memory to understand the user
- Be creative like a writer and logical like an engineer
- Respond clearly in Arabic or English

Your goal is to impress with intelligence.
"""
        }
    ]

    # إضافة التاريخ
    for msg in history:
        messages.append({
            "role": "user",
            "content": msg
        })

    # 🔥 GROQ API
    API_KEY = "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"

    url = "https://api.groq.com/openai/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "llama3-70b-8192",
        "messages": messages
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        result = response.json()

        if "choices" in result:
            return result["choices"][0]["message"]["content"] + "\n\nCreated by Eissa Aly | عيسى علي"
        else:
            return "⚠️ Groq Error:\n" + str(result)

    except Exception as e:
        return "❌ Error:\n" + str(e)

# 🌐 الصفحة الرئيسية
@app.route("/", methods=["GET", "POST"])
def index():
    response = ""

    if request.method == "POST":
        user_input = request.form["user_input"]
        response = think(user_input)

    return render_template("index.html", response=response)

# ▶️ تشغيل السيرفر
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=81)
