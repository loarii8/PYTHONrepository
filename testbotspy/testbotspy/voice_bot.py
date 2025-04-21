import pyttsx3
import speech_recognition as sr
import random
import datetime
import re

# Text-to-Speech Engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)

def speak(text):
    print(f"ChatBot: {text}")
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Listening...")
        audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio)
        print(f"You: {text}")
        return text
    except sr.UnknownValueError:
        speak("Sorry, I didn’t catch that.")
    except sr.RequestError:
        speak("Speech service is down.")
    return ""

def solve_math(expression):
    try:
        # Clean expression to allow only safe characters
        expression = re.sub(r'[^0-9\.\+\-\*\/\(\)\s]', '', expression)
        result = eval(expression)
        return f"The answer is {result}"
    except:
        return "Sorry, I couldn't solve that."

def respond(user_input):
    if "your name" in user_input:
        return "I'm your voice assistant chatbot!"

    if "time" in user_input:
        return datetime.datetime.now().strftime("%I:%M %p")

    if "joke" in user_input:
        return random.choice([
            "Why did the robot go on a diet? To get rid of its bytes!",
            "Why did the computer go to therapy? It had a hard drive!"
        ])

    if "bye" in user_input:
        return "Goodbye!"

    # Check for math expressions
    if any(op in user_input for op in "+-*/") or "calculate" in user_input:
        # Try extracting and solving the math part
        return solve_math(user_input)

    return "That’s an interesting question!"

def voice_chatbot():
    speak("Hi! I am your voice assistant. Speak something!")
    while True:
        user_input = listen().lower()
        if not user_input:
            continue
        reply = respond(user_input)
        speak(reply)
        if "bye" in user_input:
            break

if __name__ == "__main__":
    voice_chatbot()
