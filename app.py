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

    # حفظ الرسالة الجديدة
    memory["users"][user_id].append(user_input)

    # آخر 5 رسائل (أفضل من 3)
    history = memory["users"][user_id][-5:]

    # حفظ الذاكرة
    with open("memory.json", "w") as f:
        json.dump(memory, f, indent=2)

    # 🧠 بناء الرسائل بشكل صحيح
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

    # 🔥 API
    API_KEY = "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"

    url = "https://openrouter.ai/api/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "openai/gpt-3.5-turbo",
        "messages": messages
    }

    try:
    result = response.json()

    if "choices" in result:
        return result["choices"][0]["message"]["content"] + "\n\nCreated by Eissa Aly | عيسى علي"
    else:
        return "⚠️ حصل خطأ من الـ API:\n" + str(result)

except Exception as e:
    return "❌ حصل Error:\n" + str(e)
