import random
import datetime

def respond(user_input):
    if "your name" in user_input:
        return "I'm your terminal chatbot!"

    if "time" in user_input:
        return datetime.datetime.now().strftime("%I:%M %p")

    if "joke" in user_input:
        return random.choice(["Why don't skeletons fight each other? They don't have the guts!",
                             "I told my computer I needed a break, and it froze!"])

    if "bye" in user_input:
        return "Goodbye! Hope to chat again soon."

    return "That's interesting. Tell me more!"

def chat():
    print("Welcome to your Terminal ChatBot!")
    while True:
        user_input = input("You: ")
        if 'bye' in user_input.lower():
            print("Goodbye!")
            break
        response = respond(user_input)
        print(f"ChatBot: {response}")

if __name__ == "__main__":
    chat()
