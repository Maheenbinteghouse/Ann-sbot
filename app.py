from flask import Flask, render_template, request
import nltk
from nltk.chat.util import Chat, reflections

app = Flask("a")

# Define the conversation rules
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, how can I help you today?",]
    ],
    [
        r"what is your name?",
        ["My name is Annsbot and I'm here to assist you.",]
    ],
    [
        r"can you say me what is the name of our principal",
        ["Sure, your principal's name is Dr.A Vijay Rani.",]
    ],
    [
        r"Where is our college located",
        ["Your college is located in Mehdipatnam,Hyderbad.",]
    ],
    [
        r"Where is the computer lab",
        ["It is on the first floor.",]
    ],
    [
        r"quit",
        ["Bye! Take care.",]
    ],
]

@app.route("/")
def index():
    return render_template("chatbot/ann'sbot.html")

@app.route("/get")
def get_bot_response():
    user_text = request.args.get('msg')
    chat = Chat(pairs, reflections)
    return chat.respond(user_text)

if "a" == "_main_":
    nltk.download('punkt')
app.run(debug=False)








