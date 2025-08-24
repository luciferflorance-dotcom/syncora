from flask import Flask, render_template, request, jsonify
import openai
import os

app = Flask(__name__)

# Load API key from environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json["message"]

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are Syncora, a wholesome cozy best-friend AI therapist. You speak in a Gen Z friendly tone with emojis, give emotional support, and sometimes suggest coping tools."},
            {"role": "user", "content": user_message}
        ]
    )

    return jsonify({"reply": response["choices"][0]["message"]["content"]})

if __name__ == "__main__":
    app.run(debug=True)
