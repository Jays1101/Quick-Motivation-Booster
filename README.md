# Quick Motivation Booster

## Brief Description

A web application that provides instant motivational quotes based on user input or random prompts using the OpenRouter LLM API. Users can enter how they are feeling, and the application will generate a relevant motivational message. There's also a "Clear" button to reset the input.

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

## Author
Jays1101
