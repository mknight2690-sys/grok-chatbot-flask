# Grok Bot - Flask Chatbot with OpenAI API

A Grok-style chatbot built with Flask and the OpenAI API. Deployable to Render in minutes.

## Features

- 🚀 Grok-style conversational AI powered by OpenAI GPT-4o-mini
- 💬 Real-time chat with conversation history
- 🌐 Responsive web UI with dark theme
- ⚡ One-click Deploy to Render

## Quick Deploy

Click the button below to deploy to Render:

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy?repo=https://github.com/mknight2690-sys/grok-chatbot-flask)

## Local Setup

```bash
# 1. Clone and install
git clone https://github.com/mknight2690-sys/grok-chatbot-flask
cd grok-chatbot-flask
pip install -r requirements.txt

# 2. Set your OpenAI API key
export OPENAI_API_KEY=your-key-here

# 3. Run locally
python app.py
```

Open http://localhost:5000 and start chatting!

## Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `OPENAI_API_KEY` | Your OpenAI API key | Yes |

## Tech Stack

| Component | Technology |
|-----------|-----------|
| AI Engine | OpenAI GPT-4o-mini (API) |
| Backend | Python + Flask |
| Deployment | Render |
| Frontend | HTML/CSS/JS |

## Project Structure

```
grok-chatbot/
├── app.py              # Flask backend with OpenAI API
├── system_prompt.txt   # Grok persona system prompt
├── requirements.txt    # Python dependencies
├── Procfile            # Render start command
├── render.yaml         # Render service config
└── static/
    ├── index.html      # Chat web UI
    └── style.css       # Styles
```
