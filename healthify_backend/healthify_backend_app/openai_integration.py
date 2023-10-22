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
        "messages": [{"role": "user", "content": "I am a healthy food enthusiast but I do not know how to make healthy food choice while cooking. I want to make a pizza. The ingredients of pizza are Flour, Salt, Sugar, Butter, Mozzarella Cheese and pepperoni. This pizza is 2000 kilocalories. I want to replace the usual ingredients for the pizza mentioned above by healthier ingredients which are less in calories so my pizza would be under 1000 kilocalories. So I choose to use Cauliflower crust instead of plain flour crust, I use less salt, I use cottage cheese instead of mozzarella cheese and chicken instead of pepperoni.\n input: Dish: Hamburger\n Calori goal: 400\n Diet: Keto"}],
        "temperature": 0.7
    }
    response = requests.post(api_url, json=data, headers=headers)
    return response.json()
