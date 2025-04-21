from flask import Flask, render_template, request
import random
import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    user_input = request.form["message"]
    reply = respond(user_input)
    return {"reply": reply}

def respond(user_input):
    if 'your name' in user_input:
        return "I'm a Flask-powered chatbot!"

    if 'time' in user_input:
        return datetime.datetime.now().strftime("%I:%M %p")

    if 'joke' in user_input:
        return random.choice(["A pun walks into a bar, ten people die. Pun in, ten dead.", "404 joke not found!"])

    return "Nice one! I'm just a Flask bot, but I'm learning 😄"

if __name__ == "__main__":
    app.run(debug=True)
