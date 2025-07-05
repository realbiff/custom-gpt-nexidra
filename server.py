from flask import Flask, jsonify
from journaling import generate_journaling_question

app = Flask(__name__)

@app.route("/generate-question", methods=["GET"])
def get_question():
    question = generate_journaling_question()
    return jsonify({"question": question})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)