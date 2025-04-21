import tkinter as tk
from tkinter import scrolledtext
import random
import datetime
import sympy as sp
from sympy.parsing.sympy_parser import parse_expr

# Basic memory
user_name = None
history = []

def respond(user_input):
    global user_name
    history.append(user_input.lower())

    if 'my name is' in user_input:
        user_name = user_input.split('my name is')[-1].strip().capitalize()
        return f"Nice to meet you, {user_name}!"

    if 'your name' in user_input:
        return "I'm your GUI-powered chatbot!"

    if 'time' in user_input:
        return f"It is {datetime.datetime.now().strftime('%I:%M %p')}."

    if 'joke' in user_input:
        return random.choice([
            "Why don’t robots panic? Because they always keep their 'cooling' systems on.",
            "I'm reading a book on anti-gravity. It's impossible to put down!"
        ])

    # Attempt symbolic math solving
    try:
        # Example: integrate(1/(1+x**2), (x, 0, sp.oo))
        if user_input.startswith("integrate"):
            expr = eval(user_input, {"__builtins__": None}, {"integrate": sp.integrate, "x": sp.Symbol('x'), "oo": sp.oo})
            return f"The result is: {expr}"

        if any(op in user_input for op in ['+', '-', '*', '/']):
            result = eval(user_input)
            return f"The answer is {result}"
    except:
        return "I couldn't solve that math problem."

    if 'bye' in user_input:
        return "Goodbye!"

    return random.choice([
        "Tell me more.",
        "Interesting...",
        "You're fun to talk to!",
        "Hmm... 🤔"
    ])

# GUI setup
def send_message():
    user_input = entry.get()
    if not user_input:
        return

    chat_window.config(state=tk.NORMAL)
    chat_window.insert(tk.END, f"You: {user_input}\n")
    entry.delete(0, tk.END)

    reply = respond(user_input)
    chat_window.insert(tk.END, f"ChatBot: {reply}\n\n")
    chat_window.config(state=tk.DISABLED)
    chat_window.yview(tk.END)

app = tk.Tk()
app.title("ChatBot GUI")

chat_window = scrolledtext.ScrolledText(app, state='disabled', width=60, height=20, bg="#f0f0f0")
chat_window.pack(padx=10, pady=10)

entry = tk.Entry(app, width=50)
entry.pack(padx=10, pady=(0, 10))
entry.bind("<Return>", lambda event: send_message())

send_button = tk.Button(app, text="Send", command=send_message)
send_button.pack()

app.mainloop()
