import openai, os
openai.api_key = os.getenv("OPENAI_API_KEY")

def get_openai_response(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a personal assistant with memory."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message['content']
