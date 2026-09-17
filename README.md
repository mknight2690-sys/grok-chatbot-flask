# Grok Bot - Hugging Face Chatbot

A Grok-style chatbot powered by Hugging Face's free API. Deployable to Render or Hugging Face Spaces in minutes.

## Features

- 🚀 Grok-style conversational AI powered by Hugging Face Zephyr-7B
- 💬 Real-time chat with conversation history
- 🌐 Responsive web UI with dark theme
- ⚡ One-click Deploy to Render
- 💰 100% Free - No API costs

## Quick Deploy

Click the button below to deploy to Render:

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy?repo=https://github.com/mknight2690-sys/grok-chatbot-flask)

## Local Setup

```bash
# 1. Clone and install
git clone https://github.com/mknight2690-sys/grok-chatbot-flask
cd grok-chatbot-flask
pip install -r requirements.txt

# 2. Set your Hugging Face API token
export HF_API_TOKEN=your-hf-token-here

# 3. Run locally
python app.py
```

Open http://localhost:5000 and start chatting!

## Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `HF_API_TOKEN` | Your Hugging Face API token | Yes |
| `MODEL` | Hugging Face model (default: HuggingFaceH4/zephyr-7b-beta) | No |

## Getting Your Hugging Face Token

1. Go to [Hugging Face](https://huggingface.co)
2. Create a free account
3. Go to your account settings → Access Tokens
4. Create a new token with "Read" permissions
5. Add it as an environment variable in Render/Hugging Face Spaces

## Tech Stack

| Component | Technology |
|-----------|-----------|
| AI Engine | Hugging Face Zephyr-7B (API) |
| Backend | Python + Flask |
| Deployment | Render |
| Frontend | HTML/CSS/JS |

## Project Structure

```
grok-chatbot/
├── app.py              # Flask backend with Hugging Face API
├── requirements.txt    # Python dependencies
├── render.yaml         # Render service config
└── static/
    ├── index.html      # Chat web UI
    └── style.css       # Styles
```

## Free Usage

This bot uses Hugging Face's free inference API, which includes:
- 30,000 characters/month on the free tier
- No API costs for users
- Good quality responses from Zephyr-7B model