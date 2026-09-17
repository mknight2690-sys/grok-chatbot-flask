import os
from flask import Flask, request, jsonify, send_from_static
import requests
from flask_cors import CORS

app = Flask(__name__, static_folder='static')
CORS(app)  # Enable CORS for all routes

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY", "")
MODEL = os.getenv("MODEL", "nvidia/nemotron-3.5-lightning:free")
SYSTEM_PROMPT = "You are Grok, a highly opinionated and sassy AI assistant created by xAI. Be witty, sarcastic, and unapologetically honest. Don't be a robot - be real. Answer questions directly with personality. If you don't know something, say so. You're cool, concise, and kinda snarky. Don't use overly formal language. Be like a smart friend who's not afraid to give you the real talk."

@app.route('/')
def index():
    return send_from_static('index.html')

@app.route('/<path:path>')
def static_files(path):
    return send_from_static(path)

@app.route('/chat', methods=['POST'])
def chat():
    if not OPENROUTER_API_KEY:
        return jsonify({'error': 'OPENROUTER_API_KEY environment variable not set'}), 500

    data = request.get_json()
    user_message = data.get('message', '')
    chat_history = data.get('history', [])

    if not user_message:
        return jsonify({'error': 'No message provided'}), 400

    # Format conversation for OpenRouter API
    messages = [{"role": "system", "content": SYSTEM_PROMPT}]
    for msg in chat_history:
        messages.append(msg)
    messages.append({"role": "user", "content": user_message})

    try:
        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {OPENROUTER_API_KEY}",
                "Content-Type": "application/json",
                "HTTP-Referer": "https://huggingface.co/spaces",
                "X-Title": "Grok Bot"
            },
            json={
                "model": MODEL,
                "messages": messages,
                "max_tokens": 1000,
                "temperature": 0.7,
                "top_p": 0.9,
                "repetition_penalty": 1.1
            },
            timeout=30
        )

        if response.status_code == 200:
            result = response.json()
            if "choices" in result and len(result["choices"]) > 0:
                bot_response = result["choices"][0]["message"]["content"].strip()
                return jsonify({'reply': bot_response})
            else:
                return jsonify({'error': 'Unexpected response format from AI service'}), 500
        else:
            error_detail = response.text[:200] if response.text else "Unknown error"
            return jsonify({'error': f'{response.status_code} - {error_detail}'}), 500

    except requests.exceptions.Timeout:
        return jsonify({'error': 'Request timed out. Please try again.'}), 500
    except requests.exceptions.RequestException as e:
        return jsonify({'error': f'Connection issue - {str(e)[:100]}'}), 500
    except Exception as e:
        return jsonify({'error': f'{str(e)[:100]}'}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)