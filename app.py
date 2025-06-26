from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "Backend is running!"

@app.route("/submit", methods=["POST"])
def submit():
    data = request.get_json()
    name = data.get("name", "Guest")
    return jsonify({"message": f"Hello {name}, your data was received!"})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)