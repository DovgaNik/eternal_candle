from flask import Flask, request, jsonify

import db
import generate_question

app = Flask(__name__)

@app.route("/gen-question")
def gen_question():
    return generate_question.generate_random_question().to_dict()

@app.get("/latest")
def get_latest():
    limit = request.args.get("limit", default=10, type=int)
    page = request.args.get("page", default=1, type=int)
    questions = db.get_latest_questions(limit, page)
    return jsonify([q.to_dict() for q in questions])

if __name__ == "__main__":
    app.run(debug=True)