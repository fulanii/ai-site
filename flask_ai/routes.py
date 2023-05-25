

from flask import render_template, request
from flask_ai import app
from .ai_backend import ask_open_ai

@app.route("/")
def home():
    return render_template("chatbot.html")


@app.route("/chat", methods=['GET', 'POST'])
def chat():
    if request.method == 'POST':
        user_chat = request.form.get("user_chat")
        answer = ask_open_ai(message=user_chat)
   
    return render_template("chatbot.html", answer=answer, user_chat=user_chat )