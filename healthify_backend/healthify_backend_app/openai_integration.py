# healthify_backend_app/openai_integration.py

import requests

def openai_request():
    api_url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer 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",
    }
    data = {
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "user", "content": "Assume you are a health concious individual who suggests healthy recipes along with its calorie count of each ingredient from the given ingredients"}],
        "temperature": 0.7
    }
    response = requests.post(api_url, json=data, headers=headers)
    return response.json()
