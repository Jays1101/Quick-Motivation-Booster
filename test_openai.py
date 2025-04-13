import openai
import os

openai.api_key = os.environ.get("OPENAI_API_KEY")
openai.api_base = "https://api.openai.com/v1"  # Explicitly set the API base

# Get the certifi CA bundle location
import certifi
certifi_path = certifi.where()
os.environ['REQUESTS_CA_BUNDLE'] = certifi_path
print(f"Certifi CA Bundle Path: {certifi_path}")
print(f"API Key being used: {openai.api_key}")

try:
    response = openai.completions.create(
        model="text-davinci-003",
        prompt="Say hello.",
        max_tokens=5
    )
    print("\nSuccessful API Call:")
    print(response)
except Exception as e:
    print(f"\nDirect OpenAI call error: {e}")