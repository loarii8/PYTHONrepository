import openai

openai.api_key = "YOUR_OPENAI_API_KEY"

def gpt_chat(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4",  # or "gpt-3.5-turbo"
        messages=[
            {"role": "system", "content": "You're a helpful and funny chatbot."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message['content'].strip()

# Try it out
while True:
    user = input("You: ")
    if user.lower() == "bye":
        break
    reply = gpt_chat(user)
    print("GPT Bot:", reply)
