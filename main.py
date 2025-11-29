import os
from functools import wraps

from flask import Flask, request, jsonify

import db
import generate_question

app = Flask(__name__)

IUBI_KEY = os.getenv("IUBI")
IUBIT_KEY = os.getenv("IUBIT")


def require_auth(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        auth_key = request.cookies.get("auth_key")

        if not auth_key:
            return jsonify({"error": "Missing auth cookie"}), 401

        if auth_key not in [IUBI_KEY, IUBIT_KEY]:
            return jsonify({"error": "Invalid key"}), 403

        return f(*args, **kwargs)

    return wrapper


@app.post("/gen-question")
@require_auth
def gen_question():
    return generate_question.generate_random_question().to_dict()


@app.get("/latest")
@require_auth
def get_latest():
    limit = request.args.get("limit", default=10, type=int)
    page = request.args.get("page", default=1, type=int)
    questions = db.get_latest_questions(limit, page)
    return jsonify([q.to_dict() for q in questions])


@app.get("/question")
@require_auth
def get_question():
    question_id = request.args.get("question_id", type=str)
    question = db.get_question(question_id)
    return jsonify(question.to_dict())


@app.put("/response")
@require_auth
def respond():
    auth_key = request.cookies.get("auth_key")
    q_id = request.args.get("question_id", type=str)
    q_response = request.args.get("question_response", type=str)

    if auth_key == IUBI_KEY:
        if db.update_iubi_response(q_id, q_response) != None:
            return "Response registered", 200
        else:
            return "Something went wrong tell me pls", 500
    if auth_key == IUBIT_KEY:
        if db.update_iubit_response(q_id, q_response) != None:
            return "Response registered", 200
        else:
            return "Something went wrong tell me pls", 500
    return None

@app.get("/cine-sunt")
@require_auth
def cine_sunt():
    auth_key = request.cookies.get("auth_key")
    if auth_key == IUBI_KEY:
        return jsonify("iubi")
    if auth_key == IUBIT_KEY:
        return jsonify("iubit")
    return None


if __name__ == "__main__":
    app.run(debug=True)
