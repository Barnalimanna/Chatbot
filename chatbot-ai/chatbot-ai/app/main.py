from flask import Flask, request, jsonify
from flask_cors import CORS  # 👈 import CORS

app = Flask(__name__)
CORS(app)  # 👈 enable CORS for all routes

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    message = data.get("message", "")

    # Example simple intent check
    if "hello" in message.lower():
        return jsonify({"response": "Hi there! How can I help you today?"})
    else:
        return jsonify({"response": "I'm not sure how to respond to that."})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
