
from flask import Flask, render_template, request, jsonify
import json
import random

app = Flask(__name__)

with open('intents.json') as file:
    data = json.load(file)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def chatbot_response():
    user_input = request.json.get("message")
    for intent in data["intents"]:
        if user_input.lower() in map(str.lower, intent["patterns"]):
            return jsonify({"response": random.choice(intent["responses"])})
    return jsonify({"response": "I'm sorry, I don't understand. Could you please rephrase?"})

if __name__ == "__main__":
    app.run(debug=True)
