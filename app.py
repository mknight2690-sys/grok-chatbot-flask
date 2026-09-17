from flask import Flask, request, jsonify
import os
from openai import OpenAI

app = Flask(__name__)

with open("system_prompt.txt", "r") as f:
    SYSTEM_PROMPT = f.read()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY", "")
)


def gpt_reply(user_msg: str, history: list = None) -> str:
    messages = [{"role": "system", "content": SYSTEM_PROMPT}]
    if history:
        messages.extend(history)
    messages.append({"role": "user", "content": user_msg})

    resp = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        max_tokens=1000,
        temperature=0.7,
    )
    return resp.choices[0].message.content.strip()


@app.route("/")
def home():
    return app.send_static_file("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    msg = data.get("message", "")
    history = data.get("history", [])
    try:
        reply = gpt_reply(msg, history)
        return jsonify({"reply": reply})
    except Exception as e:
        return jsonify({"error": str(e)})


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
