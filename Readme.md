<div align="center">

# 🎙️ Jarvis — Voice Assistant

**A homework project for the "Build Your Own AI Voice Assistant Like Alexa" bootcamp**

Built with `google-generativeai` · `gTTS` · Python

</div>

---

## Overview

Jarvis is a voice-driven AI assistant built on the exact pattern taught in the bootcamp session — take input, pass it through an LLM, speak the response back — extended with three specific upgrades assigned as homework: **memory**, **API cost savings**, and **personality**.

## ✅ Homework requirements

| # | Requirement | Implementation |
|---|---|---|
| 1 | **Memory** — the assistant should remember earlier answers in the conversation | `model.start_chat(history=[])` maintains a running chat session, so context carries across turns instead of resetting every prompt |
| 2 | **Save API cost** — simple queries shouldn't need to hit the LLM | `try_local_answer()` resolves time, date, greetings, identity, thanks, and basic math instantly, with zero API calls — a running counter tracks calls saved |
| 3 | **Personality** — responses should have style, not sound like generic AI output | A `system_instruction` locks the model into a short, witty, in-character voice on every single response |

## 📁 Files

```
.
├── voice_assistant.py              # Full script — plain Python, readable directly on GitHub
├── Voice_Assistant_Homework.ipynb  # Same code as a Colab notebook
└── README.md                       # You are here
```

## 🚀 Getting started

### 1. Install dependencies

```bash
pip install gTTS google-generativeai
```

### 2. Get an API key

Grab a free key from [Google AI Studio](https://aistudio.google.com) → **Get API key**.

### 3. Add your key

Open `voice_assistant.py` (or the notebook) and replace the placeholder:

```python
genai.configure(api_key='YOUR_API_KEY')
```

> **Never commit a real API key.** Treat it like a password — the version in this repo should always stay as the placeholder.

### 4. Run it

**In Colab:** upload `Voice_Assistant_Homework.ipynb` and run the cells top to bottom.

**Locally:**
```bash
python voice_assistant.py
```

Talk to Jarvis by typing your prompt at the `You:` line. Type `exit` to end the session.

## 🧠 How it works

```
 Your input
     │
     ▼
Does it match a local pattern?  ──Yes──▶  Answer instantly, no API call
     │
     No
     ▼
 Send to Gemini (with full chat history)
     │
     ▼
 Print + speak the response (gTTS)
```

## 🗣️ Example session

```
You: hello
Jarvis (local, no API call): Hello. Standing by.

You: what's the time
Jarvis (local, no API call): It's 06:42 PM.

You: tell me a joke about football
Jarvis: Football is the world's most efficient religion — no reading required, just 22 people
        arguing about a ball for 90 minutes.

You: exit
Jarvis: Shutting down. API calls saved this session: 2
```

## 📚 Credit

Built following the live bootcamp session by Jasbir Singh (Vedam School of Technology), using the same core tools taught in class: `input()` / `print()` fundamentals, `gTTS` for speech, and `google.generativeai` for the LLM.

To try this project, visit: https://jarvis-ai-smoky-five.vercel.app/ 
