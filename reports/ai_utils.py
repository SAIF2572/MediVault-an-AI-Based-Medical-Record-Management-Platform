import requests
import os

def analyze_report(text):

    url = "https://openrouter.ai/api/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {os.getenv('OPENROUTER_API_KEY')}",
        "Content-Type": "application/json",
        "HTTP-Referer": "http://127.0.0.1:8000",
        "X-Title": "MediVault"
    }
    print("API KEY:", os.getenv("OPENROUTER_API_KEY"))

    data = {
        "model": "deepseek/deepseek-chat",
        "messages": [
            {
                "role": "user",
                "content": f"Analyze this medical report:\n{text}"
            }
        ]
    }

    try:
        response = requests.post(url, headers=headers, json=data)

        result = response.json()
        print("API RESPONSE:", result)

        if "choices" in result:
            return "AI Generated", result["choices"][0]["message"]["content"]
        else:
            return "Error", str(result)

    except Exception as e:
        print("FULL ERROR:", str(e))

        if "blood" in text.lower():
            return "Blood Test", "Basic blood report detected"

        return "General", "AI temporarily unavailable"