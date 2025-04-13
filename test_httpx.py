import httpx
import os

api_key = os.environ.get("OPENAI_API_KEY")
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}
data = {
    "model": "text-davinci-003",
    "prompt": "Say hello.",
    "max_tokens": 5
}

try:
    response = httpx.post("https://api.openai.com/v1/completions", headers=headers, json=data)
    response.raise_for_status()  # Raise an exception for HTTP errors
    print("Successful httpx call:")
    print(response.json())
except httpx.HTTPError as e:
    print(f"httpx HTTP error: {e}")
except httpx.ConnectError as e:
    print(f"httpx Connect error: {e}")
except Exception as e:
    print(f"General httpx error: {e}")