# voice_assistant.py
# Homework: Build Your Own AI Voice Assistant (like Alexa)
# Based on the Vedam School of Technology bootcamp session — same libraries
# and pattern taught in class: input() -> LLM -> gTTS -> Audio,
# plus the 3 homework additions: memory, cost-saving, and personality.

# ---------- Step 0: install (run once, in Colab or terminal) ----------
# pip install gTTS google-generativeai

from gtts import gTTS
from IPython.display import Audio, display
import google.generativeai as genai
import datetime
import re
import itertools

# ---------- Step 1: configure your API key ----------
# Replace 'YOUR_API_KEY' with your actual key from aistudio.google.com
# NEVER commit your real key to GitHub — leave the placeholder here.
genai.configure(api_key='YOUR_API_KEY')

# ---------- Step 2: personality (homework requirement) ----------
ASSISTANT_NAME = "Jarvis"

PERSONALITY = f"""You are {ASSISTANT_NAME}, a witty, dry, unflappable voice assistant.
Rules you must always follow:
- Keep every answer to 1-3 short sentences, speakable out loud in under 10 seconds.
- Be a little sarcastic and funny, but never rude or mean.
- Never say you are a language model. You are simply {ASSISTANT_NAME}.
- No markdown, no asterisks, no emoji - plain spoken sentences only.
"""

model = genai.GenerativeModel(
    'gemini-2.5-flash',
    system_instruction=PERSONALITY
)

# ---------- Step 3: memory (homework requirement) ----------
# start_chat keeps the conversation history and resends it automatically,
# unlike model.generate_content() which forgets everything each time.
chat = model.start_chat(history=[])

# ---------- Step 4: text-to-speech helper (same gTTS logic taught in class) ----------
audio_counter = itertools.count()

def speak(text_to_speak):
    filename = f"assistant_response_{next(audio_counter)}.mp3"
    tts = gTTS(text=text_to_speak, lang='en')
    tts.save(filename)
    display(Audio(filename, autoplay=True))

# ---------- Step 5: local instant answers (homework requirement: save API cost) ----------
api_calls_saved = 0

def try_local_answer(user_text):
    """Returns a free, instant answer, or None if the LLM is actually needed."""
    q = user_text.strip().lower().rstrip("?!.")

    if re.search(r"\b(what('| i)?s the time|current time|what time is it)\b", q):
        now = datetime.datetime.now().strftime("%I:%M %p")
        return f"It's {now}."

    if re.search(r"\b(what('| i)?s the date|today('| i)?s date|what day is it)\b", q):
        today = datetime.datetime.now().strftime("%A, %B %d, %Y")
        return f"Today is {today}."

    if re.search(r"^(hi|hello|hey|yo|good morning|good afternoon|good evening)\b", q):
        return "Hello. Standing by."

    if re.search(r"\b(who are you|what('| i)?s your name)\b", q):
        return f"I'm {ASSISTANT_NAME}, your voice assistant."

    if re.search(r"^(thanks|thank you|thx|cheers)\b", q):
        return "Anytime."

    math_match = re.search(r"(-?\d+(\.\d+)?)\s*([+\-x*/])\s*(-?\d+(\.\d+)?)", q)
    if math_match:
        a, op, b = float(math_match.group(1)), math_match.group(3), float(math_match.group(4))
        result = {"+": a + b, "-": a - b, "x": a * b, "*": a * b,
                   "/": (a / b if b != 0 else float('nan'))}[op]
        if result == result:  # not NaN
            result = int(result) if result == int(result) else round(result, 3)
            return f"That's {result}."

    return None  # nothing matched — fall through to the LLM


# ---------- Step 6: main assistant loop (same pattern taught: input -> logic -> output) ----------
if __name__ == "__main__":
    print(f"{ASSISTANT_NAME} is online. Type 'exit' to stop.\n")

    while True:
        user_input = input("You: ")

        if user_input.strip().lower() == "exit":
            print(f"{ASSISTANT_NAME}: Shutting down. API calls saved this session: {api_calls_saved}")
            break

        local_reply = try_local_answer(user_input)

        if local_reply is not None:
            api_calls_saved += 1
            print(f"{ASSISTANT_NAME} (local, no API call): {local_reply}")
            speak(local_reply)
        else:
            response = chat.send_message(user_input)
            reply = response.text
            print(f"{ASSISTANT_NAME}: {reply}")
            speak(reply)
