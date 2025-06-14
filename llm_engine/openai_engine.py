import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

def get_openai_response(prompt: str, chat_history: list = None) -> str:
    messages = [{"role": "system", "content": "You are a helpful assistant."}]
    
    if chat_history:
        messages.extend(chat_history)

    messages.append({"role": "user", "content": prompt})

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=messages,
        temperature=0.7
    )

    return response.choices[0].message.content.strip()
