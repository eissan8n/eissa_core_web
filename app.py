def think(user_input):
    import json
    import requests

    # تحميل الذاكرة
    try:
        with open("memory.json", "r") as f:
            memory = json.load(f)
    except:
        memory = {"users": {}}

    user_id = "default"

    if user_id not in memory["users"]:
        memory["users"][user_id] = []

    # حفظ الرسالة
    memory["users"][user_id].append(user_input)

    # آخر 3 رسائل
    history = memory["users"][user_id][-3:]

    # حفظ
    with open("memory.json", "w") as f:
        json.dump(memory, f, indent=2)

    # 🔥 API
    API_KEY = "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"

    url = "https://openrouter.ai/api/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "openai/gpt-3.5-turbo",
        "messages": [
            {"role": "system", "content": "You are Eissa Core AI. Be smart."},
            {"role": "user", "content": str(history)}
        ]
    }

    response = requests.post(url, headers=headers, json=data)
    result = response.json()

    return result["choices"][0]["message"]["content"] + "\n\nCreated by Eissa Aly | عيسى علي"        response = think(user_input)

    return render_template("index.html", response=response, title=config["site_title"])

if __name__ == "__main__":
    app.run(debug=True)
