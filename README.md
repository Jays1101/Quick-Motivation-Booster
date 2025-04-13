# Quick Motivation Booster

## Brief Description

A web application that provides instant motivational quotes based on user input or random prompts using the OpenRouter LLM API. Users can enter how they are feeling, and the application will generate a relevant motivational message.

## Dependencies

* Python 3.x
* Flask
* requests
* python-dotenv (if you are using a `.env` file for your API key)

## Setup Instructions

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/Jays1101/Quick-Motivation-Booster.git](https://github.com/Jays1101/Quick-Motivation-Booster.git)
    ```
2.  **Navigate to the project directory:**
    ```bash
    cd quick-motivation-booster
    ```
3.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate   # On Linux/macOS
    venv\Scripts\activate.bat  # On Windows
    ```
4.  **Install dependencies:**
    ```bash
    pip install Flask requests python-dotenv
    ```
5.  **Set up the OpenRouter API key:**
    * **Option 1 (Environment Variable):** Set the `OPENROUTER_API_KEY` environment variable on your system.
    * **Option 2 (.env file):**
        * Create a `.env` file in the project root directory.
        * Add your OpenRouter API key to the `.env` file:
            ```
            OPENROUTER_API_KEY=YOUR_OPENROUTER_API_KEY
            ```
        * Make sure to install `python-dotenv` if you choose this option (`pip install python-dotenv`).
6.  **Run the application:**
    ```bash
    python app.py
    ```
7.  **Access the application:** Open your web browser and go to `http://127.0.0.1:5000/`.

## Usage

1.  Enter how you are feeling in the text box (e.g., "demotivated", "happy", "stressed").
2.  Click the "🚀 Get Inspired! 🌟" button. A motivational quote related to your input (or a random one if no input is provided) will be displayed.
3.  Use the "Clear" button to clear the text box.

## LLM API Usage

This application uses the OpenRouter API to generate motivational quotes. It sends prompts to the API based on the user's input or uses a set of default motivational prompts. The `openai/gpt-3.5-turbo` model (or another specified model) is used for generating the text responses.

## Prompts

### Default Prompts

These are the prompts used when the user clicks the "Get Inspired!" button without entering any specific feeling:
Give me a short, powerful motivational quote.
Provide a quick burst of inspiration to start my day.
What's a single thought to ignite my inner drive?
Share a concise message to encourage and uplift.
Tell me one thing to get me motivated right now.
What's a simple but profound piece of inspirational advice?
Give me a tiny spark of motivation.
Say something short to get me excited!
What's a quick phrase that radiates energy and enthusiasm?
Give me a little shout-out of excitement!
Say something that makes me feel pumped up!
Tell me something brief to cheer me up.
What's a short, happy thought to lighten my mood?
Give me a quick dose of positivity to feel better.
Say something silly and uplifting in one sentence.
What's a tiny ray of sunshine in words?
Share a very short, positive affirmation.
What's a single, optimistic thought for the moment?
Give me a quick reminder of something good.
Say one positive thing to shift my perspective.
What's a tiny nugget of positivity?
Give me a short, exciting and motivational quote.
Share a quick, cheerful and inspiring thought.
What's a tiny burst of positive energy and motivation?
Say one short thing to lift my mood and inspire me.
Give me a quick, exciting and positive affirmation.

**Design Explanation:** These prompts are designed to be varied, covering different aspects of motivation, inspiration, excitement, and positivity. They are all short and direct to encourage concise and impactful responses from the LLM. The variety ensures that the user gets a different flavor of encouragement each time they click the button without providing input.

### Dynamic Prompt

When the user enters a feeling in the text box, the following structure is used to generate a prompt:
Give me an instant short motivational quote for someone feeling [user_input].

**Design Explanation:** This prompt is designed to tailor the motivational message to the user's specific emotional state. By including the `[user_input]` (which is replaced with the user's actual text), the LLM is instructed to provide a more relevant and empathetic response. The request for an "instant short" quote ensures that the response remains concise and immediately uplifting.

## Author
Jays1101
