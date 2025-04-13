from flask import Flask, render_template, request
import requests
import os
import random

app = Flask(__name__)
OPENROUTER_API_KEY = os.environ.get("OPENROUTER_API_KEY")
OPENROUTER_BASE_URL = "https://openrouter.ai/api/v1"

default_prompts = [
    # General Motivation & Inspiration
    "Give me a short, powerful motivational quote.",
    "Provide a quick burst of inspiration to start my day.",
    "What's a single thought to ignite my inner drive?",
    "Share a concise message to encourage and uplift.",
    "Tell me one thing to get me motivated right now.",
    "What's a simple but profound piece of inspirational advice?",
    "Give me a tiny spark of motivation.",

    # Excitement
    "Say something short to get me excited!",
    "What's a quick phrase that radiates energy and enthusiasm?",
    "Give me a little shout-out of excitement!",
    "Say something that makes me feel pumped up!",

    # Cheer Up & Mood Lightening
    "Tell me something brief to cheer me up.",
    "What's a short, happy thought to lighten my mood?",
    "Give me a quick dose of positivity to feel better.",
    "Say something silly and uplifting in one sentence.",
    "What's a tiny ray of sunshine in words?",

    # Positivity
    "Share a very short, positive affirmation.",
    "What's a single, optimistic thought for the moment?",
    "Give me a quick reminder of something good.",
    "Say one positive thing to shift my perspective.",
    "What's a tiny nugget of positivity?",

    # Combining Themes
    "Give me a short, exciting and motivational quote.",
    "Share a quick, cheerful and inspiring thought.",
    "What's a tiny burst of positive energy and motivation?",
    "Say one short thing to lift my mood and inspire me.",
    "Give me a quick, exciting and positive affirmation."
]

def get_motivation(prompt):
    """Generates a short motivational message using OpenRouter API."""
    if not OPENROUTER_API_KEY:
        return "Error: OpenRouter API key not configured."

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "openai/gpt-3.5-turbo",  # You can try other models listed on OpenRouter
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 70,
        "temperature": 0.7  # Adjusted temperature for potentially more focused responses
    }

    try:
        response = requests.post(f"{OPENROUTER_BASE_URL}/chat/completions", headers=headers, json=data)
        response.raise_for_status()  # Raise an exception for bad status codes
        return response.json()['choices'][0]['message']['content'].strip()
    except requests.exceptions.RequestException as e:
        print(f"OpenRouter API Error: {e}")
        return f"Error generating motivation via OpenRouter: {e}"

@app.route("/", methods=["GET", "POST"])
def index():
    motivation_text = None
    user_input_value = ""  # Initialize an empty string for the input field

    if request.method == "POST":
        user_input = request.form.get("user_input")
        user_input_value = user_input  # Keep the user's input in the field after submission
        # Generate a motivational quote based on user input, or a random one if no input
        if user_input:
            prompt = f"Give me an instant short motivational quote for someone feeling {user_input}."
        else:
            prompt = random.choice(default_prompts)
        motivation_text = get_motivation(prompt)
        print(f"Motivation Text: {motivation_text}")
    else:
        # For GET requests (initial load or refresh), do not generate a quote initially
        pass

    return render_template("index.html", motivation=motivation_text, user_input_value=user_input_value)

if __name__ == "__main__":
    app.run(debug=True)